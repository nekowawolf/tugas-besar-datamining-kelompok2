import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score

def main():
    url = 'https://github.com/nekowawolf/NASA-promise-dataset/raw/refs/heads/main/cm1.csv'
    df = pd.read_csv(url)

    print("Ukuran dataset:", df.shape)
    print("\nCek Missing Value:")
    print(df.isnull().sum())

    df = df.dropna()
    print("\nUkuran dataset setelah hapus missing value:", df.shape)

    df['defects'] = df['defects'].astype(int)
    X = df.drop(columns='defects')
    y = df['defects']

    scaler = MinMaxScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

    sns.countplot(x=y_resampled)
    plt.title('Distribusi Label setelah SMOTE')
    plt.tight_layout()
    plt.savefig("label_distribution_after_smote.png")
    plt.close()

    df_final = X_scaled.copy()
    df_final['defects'] = y.values
    correlations = df_final.corr()['defects'].drop('defects')
    correlations.sort_values(ascending=False).plot(kind='bar', figsize=(12, 5))
    plt.title('Korelasi Fitur terhadap Target (defects)')
    plt.ylabel('Korelasi')
    plt.tight_layout()
    plt.savefig("feature_correlation.png")
    plt.close()

    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

    models = {
        "Logistic Regression": LogisticRegression(),
        "Random Forest": RandomForestClassifier(),
        "K-Nearest Neighbors": KNeighborsClassifier()
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"\nModel: {name}")
        print("Akurasi:", acc)
        print(classification_report(y_test, y_pred, zero_division=0))

if __name__ == "__main__":
    main()
