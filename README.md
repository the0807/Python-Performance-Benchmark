<div align="center">

# Python-Performance-Benchmark

### 🧐 Comparing Python 3.10, 3.13 and 3.13(Free-threaded Mode) processing speed

</div>

# 🖥️ Environment
<div align="center">

|OS|CPU|RAM|Python|
|:---:|:---:|:---:|:---:|
|Ubuntu 22.04|Intel(R) Core(TM)<br> i5-8500B CPU @ 3.00GHz|8GB|3.10.16,<br>3.13.1t|

</div>

# 🏆 Performance


> [!Note]
> - GIL deactivation of Python 3.13 seems to be less optimized than `pypy` or `cython` yet

# ✏️ Prepare
1. Create Python 3.10, Python 3.13 environments with Anaconda and pyenv

    ``` shell
    # Python 3.10
    conda create -n bechpy3.10 python=3.10

    # Python 3.13
    pyenv install 3.13.1t
    ```

> [!Tip]
> - `Python 3.13.1t` has GIL disabled by default and can be turned on through arguments

# 📚 Usage
### ⭐ Python 3.13(Free-threaded Mode)
> [!Important]
> - Please make sure it's a `Python 3.13` environment

### 1. Check GIL activity

``` shell
python GIL_check.py
```

> [!Tip]
> - If the output is `False`, GIL is disabled

### 2. Run benchmark

``` shell
python bench.py
```

### ⭐ Python 3.13
> [!Important]
> - Please make sure it's a `Python 3.13` environment

### 1. Run benchmark

``` shell
python -X gil=1 bench.py
```

> [!Tip]
> - `-X gil=1` argument activates GIL
> - In `Python 3.13.1t`, GIL is inactive by default and can be specified as `gil=0`

### ⭐ Python 3.10
> [!Important]
> - Please make sure it's a `Python 3.10` environment

### 1. Run benchmark

``` shell
python bench.py
```
