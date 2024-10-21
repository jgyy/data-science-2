import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine

def connect_to_db():
    # Replace with your actual database connection details
    engine = create_engine('postgresql://username:password@host:port/database')
    return engine

def get_data(engine):
    query = """
    SELECT event_type, COUNT(*) as count
    FROM your_table_name
    GROUP BY event_type
    """
    return pd.read_sql(query, engine)

def create_pie_chart(data):
    plt.figure(figsize=(10, 8))
    plt.pie(data['count'], labels=data['event_type'], autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Site Activity Distribution')
    plt.savefig('pie.png')
    plt.close()

def main():
    engine = connect_to_db()
    data = get_data(engine)
    create_pie_chart(data)
    print("Pie chart has been created and saved as 'pie.png'")

if __name__ == "__main__":
    main()
