import sqlite3

class Data_Storage:
  def __init__(self, db_file):
    self.connection = sqlite3.connect(db_file)
    self.cursur = self.connection.cursor()
    self.create_tables()
  
  def create_tables(self):
    self.cursur.execute('''CREATE TABLE IF NOT EXISTS categories(
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        name TEXT NOT NULL,
                        category_limit REAL NOT NULL)''')
    
    self.cursur.execute('''CREATE TABLE IF NOT EXISTS expenses(
                        id INTEGER PRIMARY KEY,
                        category_id INTEGER,
                        value REAL NOT NULL,
                        description TEXT NOT NULL, 
                        FOREIGN KEY(category_id) REFERENCES category(id))''')
    
    self.connection.commit()

  def add_category(self, name, limit):
    self.cursur.execute('INSERT INTO categories (name, category_limit) VALUES (?, ?)', (name, limit))
    self.connection.commit()

  def add_expense(self, category_name, value, description):
    self.cursur.execute('SELECT id FROM categories WHERE name = ?', (category_name,))
    category_id = self.cursur.fetchone()

    if category_id:
      self.cursur.execute('INSERT INTO expenses (category_id, value, description) VALUES (?, ?, ?)', 
                          (category_id[0], value, description))
      self.connection.commit()

  def get_all_categories(self):
    self.cursur.execute('SELECT name, category_limit FROM categories')
    return self.cursur.fetchall()
  
  def get_expenses_for_category(self, category_name):
    self.cursur.execute('SELECT id FROM categories WHERE name = ?', (category_name,))
    category_id = self.cursur.fetchall()

    if category_id:
      self.cursur.execute('SELECT value, description FROM expenses where category_id = ?', (category_id[0]))
      return self.cursur.fetchall()
    
  def fetch_data(self):
    import budget as b
    budget = b.Budget(revenue=1000)

    categories = self.get_all_categories()
    for category in categories:
      tmp_category = b.Budget_Category(name=category[0], limit=category[1])
      expenses = self.get_expenses_for_category(category_name=category[0])
      for expense in expenses:
        tmp_category.add_expense(value=expense[0], description=expense[1])
      budget.add_category(tmp_category)

    return budget