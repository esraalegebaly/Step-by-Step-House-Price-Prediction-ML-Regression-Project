{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "import pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n\ndataset = pd.read_excel(\"HousePricePrediction.xlsx\")\n\n# Printing first 5 records of the dataset\nprint(dataset.head(5))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "ename": "<class 'ModuleNotFoundError'>",
          "evalue": "No module named 'seaborn'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "Cell \u001b[0;32mIn[8], line 3\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mmatplotlib\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpyplot\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mplt\u001b[39;00m\n\u001b[0;32m----> 3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mseaborn\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01msns\u001b[39;00m\n\u001b[1;32m      5\u001b[0m dataset \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_excel(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mHousePricePrediction.xlsx\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m      7\u001b[0m \u001b[38;5;66;03m# Printing first 5 records of the dataset\u001b[39;00m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'seaborn'"
          ],
          "output_type": "error"
        }
      ],
      "execution_count": 8
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}