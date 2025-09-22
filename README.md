
# **LAB 1 – MLOps (IE-7374): GitHub (Lab-1)**

### **Objective**

The objective of this lab was to learn the fundamentals of GitHub for managing machine learning projects. The lab covered setting up a virtual environment, creating and cloning a GitHub repository, organizing project structure, implementing Python code, writing tests using `pytest` and `unittest`, and automating workflows with GitHub Actions.

---

### **Step 1: Virtual Environment Setup**

* Created a project folder `mlops_lab` in the local system.
* Initialized a virtual environment using:

  ```bash
  python -m venv lab_01
  lab_01\Scripts\activate
  ```
* This ensured dependencies were isolated from the global Python environment.

---

### **Step 2: GitHub Repository Creation & Cloning**

* A new GitHub repository named **mlops-lab1** was created with a `README.md`.
* The repository was cloned into the local project folder using:

  ```bash
  git clone <repository_url>
  ```
* Inside the repo, the following structure was created:

  ```
  src/        → source code
  test/       → test scripts
  data/       → data files
  .github/    → GitHub Actions workflows
  ```

---

### **Step 3: Python Code Implementation**

* A Python script `bmi.py` was added inside the `src/` folder.
* It contained two functions:

  ```python
  def bmi(weight, height):  # calculates BMI
  def category(bmi_value):  # returns BMI category
  ```
* These functions implemented basic health-related calculations.

---

### **Step 4: Writing Tests**

* Two types of test files were created inside the `test/` folder.

  * **Pytest** (`test_bmi_pytest.py`): used assertions to validate outputs.
  * **Unittest** (`test_bmi_unittest.py`): used test classes with `assertEqual`.
* Both test files were configured to locate the `src` folder correctly.

---

### **Step 5: Running Tests Locally**

* Installed `pytest` and created a `requirements.txt`.
* Verified tests by running:

  ```bash
  pytest
  python test\test_bmi_unittest.py
  ```
* Both test suites executed successfully with all test cases passing.

---

### **Step 6: GitHub Actions Workflows**

* Two workflows were created in `.github/workflows/`:

  * `pytest_action.yml` → runs pytest automatically on every push.
  * `unittest_action.yml` → runs unittest automatically on every push.
* These workflows install dependencies, run tests, and report results in GitHub.

---

### **Step 7: Automation Verification**

* After pushing code and workflows to GitHub, both workflows were triggered automatically.
* Verified under the **Actions** tab in GitHub.
* Both workflows passed successfully (green check marks ✅), confirming automation worked.

---

### **Conclusion**

This lab demonstrated the complete lifecycle of setting up a Python project with GitHub for MLOps:

* Created a virtual environment for dependency management.
* Organized code into a clean folder structure.
* Implemented Python functions and validated them with tests.
* Automated the testing process using GitHub Actions.

With this workflow, every future code change will be automatically tested before integration, ensuring reliability and reproducibility — a key principle of MLOps.

