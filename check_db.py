import sqlite3
conn = sqlite3.connect('customers.db')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
print('Tables:', c.fetchall())
c.execute('SELECT COUNT(*) FROM customer_data')
print('Total Rows:', c.fetchone()[0])
c.execute('PRAGMA table_info(customer_data)')
cols = c.fetchall()
print('Columns:')
for col in cols:
    print(' ', col)
c.execute('SELECT * FROM customer_data LIMIT 3')
print('Sample rows:')
for row in c.fetchall():
    print(' ', row)
conn.close()
