import data_storage as ds

class Budget_Category:
  storage = ds.Data_Storage('finanzen.db')
  def __init__(self, name, limit):
    self.name = name
    self.limit = limit
    self.expenses = []
  
  def insert_category_to_database(self):
    self.storage.add_category(name=self.name, limit=self.limit)

  def add_expense(self, value, description):
    self.expenses.append((value, description))

  def insert_expense_to_database(self, value, description):
    self.storage.add_expense(value=value, category_name=self.name, description=description)
  
  def add_new_expense(self, value, description):
    self.add_expense(value=value, description=description)
    self.insert_expense_to_database(value=value, description=description)

  def get_total_expenditure(self):
    total = 0
    for value, description in self.expenses:
      total += value
    return total
  
  def is_limit_exceeded(self):
    total = self.get_total_expenditure()
    return total > self.limit

  def __str__(self):
    return f"\nKategorie: {self.name}\nLimit: {self.limit}\nGesamtausgaben: {self.get_total_expenditure()}\n"

class Budget:
  def __init__(self, revenue):
    self.revenue = revenue
    self.category = []
  
  def add_category(self, category):
    self.category.append(category)
  
  def remove_category(self, category_name):
    for category in self.category:
      if category_name == category.name:
        self.category.remove(category)
        print(f"Kategorie '{category_name}' wurde erfolgreich entfernt")
        return
    print(f"Kategorie '{category_name}' nicht gefunden")
  
  def add_expenses_to_category(self, category_name, value, description):
    for category in self.category:
      if category.name == category_name:
        category.add_new_expense(value, description)
        return

    new_category = Budget_Category(name=category_name, limit=100.0)
    new_category.insert_category_to_database()
    new_category.add_expense(value=value, description=description)
    new_category.insert_expense_to_database(value=value, description=description)
    self.category.append(new_category)
  
  def get_total_expenditure(self):
    total = 0
    for category in self.category:
      total += category.get_total_expenditure()
    return total

  def get_excess(self):
    return self.revenue - self.get_total_expenditure()


