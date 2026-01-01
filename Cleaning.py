import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Customers = pd.read_csv("customers.csv")
# print(Customers.head())

Customers_Interaction = pd.read_csv("customer_interactions.csv")
# print(Customers_Interaction.head())

Loans = pd.read_csv("loans.csv")
# print(Loans.head())

Payments = pd.read_csv("payments.csv")
# print(Payments.head())

Transactions = pd.read_csv("transactions.csv")
# print(Transactions.head())

                                                    # Checking Data of Customers

# print(Customers.isnull().sum())
print(Customers.dtypes)
# print(Customers.info)
# print(Customers.describe(include="all"))
# print(Customers.shape)

                                                    # Checking Unique Values of the Column

# for col in Customers.columns:
#     if Customers[col].nunique() < 20:
#         print(Customers[col].value_counts())
#         print("-"*50)

                                                    # Checking Duplicates

# print(Customers.duplicated().sum())

# duplicates = Customers[Customers.duplicated()]
# print(duplicates)

Customers['Gender'] = Customers["Gender"].str.strip().str.title()
Customers['City'] = Customers["City"].str.strip().str.title()
Customers['Employment_Status'] = Customers["Employment_Status"].str.strip().str.title()

Customers.columns = (Customers.columns.str.strip().str.title().str.replace(' ','_'))

                                                    # Checking Outliers

# cols = ['Age', 'Income']

# plt.figure(figsize=(10,5))

# for i, col in enumerate(cols, 1):
#     plt.subplot(1,2,i)
#     sns.boxplot(y=Customers[col], color='skyblue', width=0.3)
#     plt.title(f'Boxplot of {col}', fontsize=12)
#     plt.ylabel('')
#     plt.grid(axis='y', linestyle='--', alpha=0.6)

# plt.tight_layout()
# plt.show()

                                                # Handling customers interactions table

# print(Customers_Interaction.head())
# print(Customers_Interaction.isnull().sum())
# print(Customers_Interaction.dtypes)
# print(Customers_Interaction.info())
# print(Customers_Interaction.describe(include="all"))

                                                # Showing Unique Values of the column

# for col in Customers_Interaction.columns:
#     if Customers_Interaction[col].nunique() < 20:
#         print(Customers_Interaction[col].value_counts())
#         print('---'*50)

                                                # Checking Duplicates

# print(Customers_Interaction.duplicated().sum())

                                                # Handling Another Columns

Customers_Interaction['interaction_type'] = Customers_Interaction['interaction_type'].str.strip().str.title()
Customers_Interaction['sentiment'] = Customers_Interaction['sentiment'].str.strip().str.title()

Customers_Interaction.columns = (Customers_Interaction.columns.str.strip().str.title())

                                                # Handling Loans Table

# print(Loans.head())
# print(Loans.isnull().sum())
# print(Loans.dtypes)
# print(Loans.describe(include='all'))
# print(Loans.info)

Loans['Loan_Status'] = Loans['Loan_Status'].str.strip().str.title()

Loans.columns = (Loans.columns.str.strip().str.title())

                                            # Checking Outliers
# cols = ['Loan_Amount']

# plt.figure(figsize=(10,5))

# for i, col in enumerate(cols, 1):
#     sns.boxplot(y=Loans[col], color='skyblue', width=0.3)
#     plt.title(f'Box of {col}', fontsize=12)
#     plt.ylabel('')
#     plt.grid(axis='y', linestyle='--', alpha=0.6)

# plt.tight_layout()
# plt.show()

                                            # Handling Payment Table

# print(Payments.head())
# print(Payments.isnull().sum())
# print(Payments.describe(include='all'))
# print(Payments.info)
# print(Payments.dtypes)
# print(Payments.shape)

# Changing datatypes

Payments['Due_Date'] = pd.to_datetime(Payments['Due_Date'], errors='coerce')
Payments['Payment_Date'] = pd.to_datetime(Payments['Payment_Date'], errors='coerce')

Payments.columns = (Payments.columns.str.strip().str.title())

                                            # Handling Transactions Columns

# print(Transactions.head())
# print(Transactions.isnull().sum())
# print(Transactions.describe(include='all'))
# print(Transactions.info)
# print(Transactions.dtypes)
# print(Transactions.shape)

# Changing Data types

Transactions['Transaction_Date'] = pd.to_datetime(Transactions['Transaction_Date'], errors='coerce')

Transactions['Payment_Method'] = Transactions['Payment_Method'].str.strip().str.title()

Transactions.columns = (Transactions.columns.str.strip().str.title())


# Customers_Interaction.to_csv('Customer_Transaction.csv', index=False)
# Customers.to_csv('Customers01.csv', index=False)
# Loans.to_csv('Loans01.csv', index=False)
# Payments.to_csv('Payments01.csv', index=False)
# Transactions.to_csv('Transactions01.csv', index=False)



