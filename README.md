# asgmt-06-python-for-non-stem
Assignment 06: Python for Non-STEM.

## 練習題指引

- 將練習題的 GitHub Repository 下載到自己的電腦，解壓縮後以 VS Code 開啟專案資料夾。
- 先閱讀 `README.md`，再將答案寫在 `answers.py`
- 練習題共分為三種：
  - 是非題：預設答案 `answer_01 = None`，請以布林型別宣告答案，若覺得是非題的敘述**不正確**，就宣告 `answer_01 = False`，若覺得是非題的敘述**正確**則宣告 `answer_01 = True`
  - 單選題：預設答案 `answer_02 = None`，請以整數型別宣告答案，若覺得單選題的第一個選項**正確**宣告為 `answer_02 = 1`，若覺得單選題的第二個選項**正確**則宣告 `answer_02 = 2`，若覺得單選題的第三個選項**正確**則宣告 `answer_02 = 3`，若覺得單選題的第四個選項**正確**則宣告 `answer_02 = 4`
  - 程式題：以函數/類別宣告答案，函數/類別名稱下的長字串（docstring）會描述測試資料與預期輸出，能夠讓我們充分暸解預期輸入以及預期輸出之間的對應關係，寫作完畢後要記得輸出答案的變數 `return your_answer_variable`
- 如果練習題需要載入檔案，檔案會與練習題存放在同個資料夾中，這時可以運用工作目錄的相對路徑直接指定檔案名稱載入。
- 寫作完成後將 `answers.py` 存檔，再執行專案資料夾中的 `test_runner.py` 進行測試，再依照測試結果修正答案或截圖測試結果繳交作業。

## 01.（程式題）定義函數 `answer_01()` 能夠將輸入的彈性參數做是否為質數的判斷。

來源：<https://en.wikipedia.org/wiki/Prime_number>

```python
def answer_01(*args) -> list:
    """
    >>> answer_01(1, 2, 3)
    [False, True, True]
    >>> answer_01(4, 5, 6)
    [False, True, False]
    >>> answer_01(7, 11, 13, 17, 19)
    [True, True, True, True, True]
    >>> answer_01(20, 21, 22, 24, 25, 26, 27)
    [False, False, False, False, False, False, False]
    """
```

## 02.（程式題）定義函數 `answer_02()` 能夠篩選輸入正整數範圍內的質數。

來源：<https://en.wikipedia.org/wiki/Prime_number>

```python
def answer_02(begin: int, end: int) -> list:
    """
    >>> answer_02(1, 5)
    [2, 3, 5]
    >>> answer_02(6, 10)
    [7]
    >>> answer_02(11, 15)
    [11, 13]
    """
```

## 03.（程式題）定義函數 `answer_03()` 能夠回傳前 n 個質數。

來源：<https://en.wikipedia.org/wiki/Prime_number>

```python
def answer_03(n: int) -> list:
    """
    >>> answer_03(5)
    [2, 3, 5, 7, 11]
    >>> answer_03(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> answer_03(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    """
```

## 04.（程式題）定義函數 `answer_04()` 能夠從彈性參數中挑出負數再平方。

```python
def answer_04(*args) -> list:
    """
    >>> answer_04(-3, -2, -1, 0, 1, 2, 3)
    [9, 4, 1]
    >>> answer_04(-3, 0, 1, 2, 3, -2, -1)
    [9, 4, 1]
    >>> answer_04(0, 1, 2, 3, -1, -2, -3)
    [1, 4, 9]
    """
```

## 05.（程式題）定義函數 `answer_05()` 能夠從彈性參數中把鍵與值都轉換為大寫英文。

```python
def answer_05(**kwargs) -> dict:
    """
    >>> answer_05(tw="twn")
    {'TW': 'TWN'}
    >>> answer_05(tw="twn", jp="jpn")
    {'TW': 'TWN', 'JP': 'JPN'}
    >>> answer_05(tw="twn", jp="jpn", lt="ltu")
    {'TW': 'TWN', 'JP': 'JPN', 'LT': 'LTU'}
    """
```