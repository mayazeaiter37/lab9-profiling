# Lab 9 – Profiling in Python

Maya Zeaiter – EECE 435L

- `before_optimization/` – original scripts from the lab sheet (`profiler.py`, `profiler_lineprofiler.py`, `profiler_memoryprofiler.py`, `test_profiler.py`) and their coverage HTML report (`htmlcov/index.html`).
- `after_optimization/` – optimized versions (`optimized_fast_function`, O(1) sum-of-squares formula instead of the 10M-iteration loop), extra tests, and their coverage HTML report.
- `outputs/` – raw text output of every profiler/test run.
- `screenshots/` – terminal screenshots of every run.
- `lab9_Maya_Zeaiter.docx` – report with screenshots and analysis.

## Run

```bash
pip install line_profiler memory_profiler coverage
cd before_optimization   # or after_optimization
python3 -m cProfile -s time profiler.py
python3 profiler_lineprofiler.py
python3 -m memory_profiler profiler_memoryprofiler.py
coverage run -m unittest discover && coverage report -m && coverage html
```
