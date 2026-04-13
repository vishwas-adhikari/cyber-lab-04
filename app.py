from flask import Flask, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "super_secret_lab_key"

def init_db():
    conn = sqlite3.connect('lab.db')
    c = conn.cursor()
    # Ensure fresh start for the lab
    c.execute('DROP TABLE IF EXISTS employees')
    c.execute('DROP TABLE IF EXISTS hidden_flags')
    c.execute('CREATE TABLE employees (id INTEGER, name TEXT, department TEXT)')
    c.execute('CREATE TABLE hidden_flags (id INTEGER, flag_value TEXT, description TEXT)')
    
    # Populate data
    c.execute("INSERT INTO employees VALUES (1, 'Alice', 'HR')")
    c.execute("INSERT INTO employees VALUES (2, 'Bob', 'IT')")
    c.execute("INSERT INTO employees VALUES (3, 'Charlie', 'Engineering')")
    c.execute("INSERT INTO hidden_flags VALUES (99, 'FLAG{Burp_M4st3r_And_SQLi_N1nj4}', 'Top Secret')")
    
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # VULNERABILITY: Trusting the hidden 'role' input
        session['role'] = request.form.get('role', 'guest')
        return redirect(url_for('dashboard'))
    
    return '''
    <html><body style="font-family: Arial; text-align: center; margin-top: 50px;">
        <h2>Corporate Employee Portal</h2>
        <!-- Hint for cURL users: To become admin, you must send a POST request changing the hidden role value to 'admin' -->
        <form method="POST" action="/">
            <input type="hidden" name="role" value="guest">
            <button type="submit" style="padding: 15px; font-size: 18px;">Continue as Guest</button>
        </form>
    </body></html>
    '''

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    role = session.get('role', 'guest')
    conn = sqlite3.connect('lab.db')
    c = conn.cursor()

    if role == 'guest':
        c.execute("SELECT * FROM employees")
        data = c.fetchall()
        return f"<html><body><h2>Guest Dashboard (Read-Only)</h2><p>Employee Data: {data}</p><a href='/logout'>Logout</a></body></html>"
    
    elif role == 'admin':
        search_query = request.form.get('search', '')
        error_msg = ""
        data = []
        
        if search_query:
            # VULNERABILITY: SQL Injection via f-string (No sanitization)
            sql = f"SELECT id, name, department FROM employees WHERE name = '{search_query}'"
            try:
                c.execute(sql)
                data = c.fetchall()
            except Exception as e:
                error_msg = f"SQL Error: {str(e)}"
        else:
            c.execute("SELECT id, name, department FROM employees")
            data = c.fetchall()
            
        return f'''
        <html><body style="font-family: Arial; background-color: #f4f4f9;">
            <h2 style="color: red;">Admin Dashboard (Full Access)</h2>
            <form method="POST">
                Search Employee: <input type="text" name="search">
                <button type="submit">Search</button>
            </form>
            <p style="color: red;">{error_msg}</p>
            <h3>Results:</h3>
            <table border="1" cellpadding="5"><tr><th>ID</th><th>Name</th><th>Dept</th></tr>
            {"".join(f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>" for row in data)}
            </table>
            <br><a href='/logout'>Logout</a>
        </body></html>
        '''
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=80)
