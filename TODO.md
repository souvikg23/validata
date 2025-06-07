
# TODO List for Validata

MVP Design and Project Structure  
Core DataCleaner class skeleton  
Parallel processing support (column-level parallelism)  
Scheduling support (daily/hourly)  
Basic HTML profile report  
LLM type inference stub  
Schema inference utilities  

🚧 In Progress:
- Implement core cleaning functions:
  - Impute missing values
  - Remove outliers
  - Column name fixes
- Implement schema validation rules
- Improve profile report visuals (matplotlib / seaborn / plotly)
- Write example notebook for GitHub demo
- Initial test coverage (pytest)
- Improve error reporting UX

💡 Future Ideas:
- Support Dask / Spark backends
- CLI tool for running clean + validate pipelines from terminal
- Streamlit UI for interactive use
- Statistical anomaly detection module
- Data lineage & audit logging
- Deployment helpers for CI/CD pipelines
