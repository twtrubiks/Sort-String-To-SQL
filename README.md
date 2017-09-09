# Sort-String-To-SQL

Sort String To SQL For Python 📝

參考 [sortStringToSql](https://github.com/killercup/sortStringToSql) 修改為 Python 版本

## 說明

將 'sort expressions' 轉換成 SQL expressions，方便資料庫 ORDER BY 欄位， E.g.  `+id` 會被轉換為 `id ASC`，

因為我目前使用 [MySQL](https://www.mysql.com/downloads/) 居多，所以不同資料庫寫法可能有稍微不同，請在自行修改或 Issuse 給我 :smile:

## 範例

可參考  [sort_string_to_sql.py]()

```python
print('+id ->', sort_str_to_sql(sort_expression='+id'))
## +id -> id ASC

print('+id,-name ->', sort_str_to_sql(sort_expression='+id,-name'))
## +id,-name -> id ASC, name DESC

print(' ->', sort_str_to_sql(sort_expression=''))
##   ->
```

更多範例可參考 [tests.py]()

## Test By Case

目前是 by case 寫測試，可參考 [tests.py]()

請在命令提示字元  ( cmd ) 底下輸入

```python
 python -m unittest -v tests
```

output

```cmd
test_case_1 (tests.TestCase) ... ok
test_case_2 (tests.TestCase) ... ok
test_case_3 (tests.TestCase) ... ok
test_case_4 (tests.TestCase) ... ok
test_case_5 (tests.TestCase) ... ok
test_case_6 (tests.TestCase) ... ok
test_case_7 (tests.TestCase) ... ok
test_case_8 (tests.TestCase) ... ok
test_case_9 (tests.TestCase) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

## 執行環境

* Python 3.6.2

## Reference

* [sortStringToSql](https://github.com/killercup/sortStringToSql)

## License

MIT license
