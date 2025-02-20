# Customer Segmentation Using K-Means Clustering

This repository contains a Python script that performs customer segmentation using the K-Means clustering algorithm. The script uses the `pandas` library for data manipulation, `scikit-learn` for clustering, and `matplotlib` for visualization. The dataset used in this project contains customer information from a mall, including annual income and spending scores. The goal is to group customers into distinct segments based on their purchasing behavior.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Visualization](#visualization)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

Customer segmentation is a crucial technique in marketing and business analytics. By grouping customers with similar behaviors, businesses can tailor their strategies to meet the needs of each segment effectively. This project uses the **K-Means clustering algorithm** to segment mall customers based on their **Annual Income** and **Spending Score**. The results are visualized to provide insights into customer behavior.

---

## Requirements

To run this code, you need the following Python libraries installed:

- `pandas`
- `scikit-learn`
- `matplotlib`

You can install these libraries using pip:

```bash
pip install pandas scikit-learn matplotlib
```

---

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/customer-segmentation.git
```

2. Navigate to the project directory:

```bash
cd customer-segmentation
```

3. Ensure you have the required libraries installed (see [Requirements](#requirements)).

---

## Usage

1. Place the dataset (`Mall_Customers.csv`) in the project directory.

2. Run the script:

```bash
python customer_segmentation.py
```

3. The script will generate a scatter plot visualizing the customer segments and their centroids.

---

## Code Overview

The script performs the following steps:

1. **Import Libraries**: The necessary libraries are imported, including `pandas` for data manipulation, `scikit-learn` for clustering, and `matplotlib` for visualization.

2. **Load Dataset**: The dataset is loaded from `Mall_Customers.csv` using `pandas`.

3. **Feature Selection**: Relevant features for clustering are selected, specifically `Annual Income (k$)` and `Spending Score (1-100)`.

4. **K-Means Clustering**: The K-Means algorithm is applied to the data with 5 clusters. The resulting cluster labels are added to the dataset.

5. **Visualization**: A scatter plot is created to visualize the clusters. Each cluster is represented by a different color, and the centroids are marked with a black "X".

6. **Plot Details**: The plot is customized with a title, axis labels, and a legend for better interpretation.

---

## Visualization

The script generates a scatter plot that visualizes the customer segments based on their **Annual Income** and **Spending Score**. Here's what the plot includes:

- **Clusters**: Each cluster is represented by a different color, showing groups of customers with similar purchasing behavior.
- **Centroids**: The centroids of each cluster are marked with a black "X", representing the center of each group.
- **Labels**: The plot includes axis labels and a legend for clarity.

### Example Output:
![Customer Segmentation Plot](example_plot.png)

---

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify this README to better suit your project's needs. Happy clustering! 🚀
