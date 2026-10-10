# Databricks notebook source
# MAGIC %md
# MAGIC # DAB Shared Deployment Test Notebook

# COMMAND ----------
print("Hello World! This notebook was deployed via a Service Principal DAB notebook 2")

# COMMAND ----------
# Check the notebook's runtime path to see exactly where it landed
import os
print(f"Current Notebook Path: {dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()}")
