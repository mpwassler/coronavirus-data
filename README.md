# Playing around with some coronavirus data.
## Inspiration and resources
[ourworldindata](https://ourworldindata.org/coronavirus)

[ncov.bii.virginia.edu](http://ncov.bii.virginia.edu/dashboard)
## App

Build with `docker-compose build app`

In order to get the data you will need to run `docker-compose run app python import.py`. The data is from [ncov.bii.virginia.edu](http://ncov.bii.virginia.edu/dashboard). They have a lot more information on their website. I only did this beacuse I wanted to plot the percentages of increase.

Run with `docker-compose run app python app.py`

Will defualt to USA. You can run for other countries by passing them as a paramiter.

Run with `docker-compose run app python app.py "Mainland China"`

It supports states / sub regions by adding them after the country like `docker-compose run app python app.py "USA" "New York"`

Will print a table like (Italy)
```
+------------+-------+-----------+--------+------------+-----------+-------------------+--------------------+
|    Date    | Cases | Cases % ^ | Deaths | Deaths % ^ | Recovered | % cases recovered | Case Fatality Rate |
+------------+-------+-----------+--------+------------+-----------+-------------------+--------------------+
| 02-21-2020 |   20  |    85.0   |   1    |   100.0    |     0     |        0.0        |        5.0         |
| 02-22-2020 |   79  |   74.684  |   2    |    50.0    |     1     |       1.2658      |       2.5316       |
| 02-23-2020 |  157  |   49.682  |   3    |   33.333   |     2     |       1.2739      |       1.9108       |
| 02-24-2020 |  229  |   31.441  |   7    |   57.143   |     1     |       0.4367      |       3.0568       |
| 02-25-2020 |  323  |   29.102  |   11   |   36.364   |     1     |       0.3096      |       3.4056       |
| 02-26-2020 |  470  |   31.277  |   12   |   8.333    |     3     |       0.6383      |       2.5532       |
| 02-27-2020 |  655  |   28.244  |   17   |   29.412   |     45    |       6.8702      |       2.5954       |
| 02-28-2020 |  889  |   26.322  |   21   |   19.048   |     46    |       5.1744      |       2.3622       |
| 02-29-2020 |  1128 |   21.188  |   29   |   27.586   |     46    |       4.078       |       2.5709       |
| 03-01-2020 |  1694 |   33.412  |   34   |   14.706   |     83    |       4.8996      |       2.0071       |
| 03-02-2020 |  2036 |   16.798  |   52   |   34.615   |    149    |       7.3183      |       2.554        |
| 03-03-2020 |  2502 |   18.625  |   79   |   34.177   |    160    |       6.3949      |       3.1575       |
| 03-04-2020 |  3089 |   19.003  |  107   |   26.168   |    276    |       8.9349      |       3.4639       |
| 03-05-2020 |  3858 |   19.933  |  148   |   27.703   |    414    |      10.7309      |       3.8362       |
| 03-06-2020 |  4636 |   16.782  |  197   |   24.873   |    523    |      11.2813      |       4.2494       |
| 03-07-2020 |  5883 |   21.197  |  233   |   15.451   |    589    |      10.0119      |       3.9606       |
| 03-08-2020 |  7375 |   20.231  |  366   |   36.339   |    622    |       8.4339      |       4.9627       |
| 03-09-2020 |  9172 |   19.592  |  463   |   20.95    |    724    |       7.8936      |       5.048        |
| 03-10-2020 | 10149 |   9.627   |  631   |   26.624   |    1004   |       9.8926      |       6.2174       |
| 03-11-2020 | 12462 |   18.56   |  827   |    23.7    |    1045   |       8.3855      |       6.6362       |
| 03-12-2020 | 15113 |   17.541  |  1016  |   18.602   |    1258   |       8.324       |       6.7227       |
| 03-13-2020 | 17660 |   14.422  |  1266  |   19.747   |    1439   |       8.1484      |       7.1687       |
| 03-14-2020 | 21157 |   16.529  |  1441  |   12.144   |    1966   |       9.2924      |       6.811        |
| 03-15-2020 | 24747 |   14.507  |  1809  |   20.343   |    2335   |       9.4355      |        7.31        |
| 03-16-2020 | 27980 |   11.555  |  2158  |   16.172   |    2749   |       9.8249      |       7.7127       |
| 03-17-2020 | 31506 |   11.192  |  2503  |   13.783   |    2749   |       8.7253      |       7.9445       |
| 03-18-2020 | 35713 |   11.78   |  2978  |   15.95    |    4205   |      11.7744      |       8.3387       |
| 03-19-2020 | 41035 |   12.969  |  3405  |   12.54    |    4440   |       10.82       |       8.2978       |
| 03-20-2020 | 47021 |   12.73   |  4032  |   15.551   |    4440   |       9.4426      |       8.5749       |
| 03-21-2020 | 53578 |   12.238  |  4825  |   16.435   |    6072   |       11.333      |       9.0056       |
+------------+-------+-----------+--------+------------+-----------+-------------------+--------------------+
```

Showing percent increase by day.

Will also genertate a plot as a png file like 

![data plot](charts/growth_rate.png)
![data plot](charts/totals.png)