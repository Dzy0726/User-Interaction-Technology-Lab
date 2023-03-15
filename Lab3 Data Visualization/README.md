# Lab 3: Data Visualization

## How to Run

1. Start the server by running app.py

   ``` 
   python app.py
   ```

2. Once the server starts up, access [http://localhost:8050](http://localhost:8050/) to get the UI.

3. Choose the item from the **Dropdown**, and you will see the graph which hold the data which come from this item only.

4. You can Download plot as a png, Zoom, Pan, Box Select, Lasso Select, Zoom in, Zoom out, Auto scale Reset axes, Toggle Spike Lines, Show closest data on hover, Compare data on hover, which are powered by the DASH.

## Development Environment

- **Development Environment:** Mac OS Catalina 10.15.7

- **Development Software:**

  1. **PyCharm** *2019.1.1.PC-191.6605.12*
  2. **Visual Studio Code** 1.33.1.0

- **Development Language:**

  ​	python3

- **Mainly Reference Count:**

  1. dash(dash_core_components, dash_html_components, dash_daq)
  2. dash.dependencies (Input, Output, State)
  3. pandas
  4. plotly(plotly.graph_objs)
  5. csv

## Data Analysis Task

### Objectives

I choose the `BlackFriday` as the database to proceed the Data Visualization task.

This data set shows the details of customers, such as gender, age group, type of work (number), city category (grade), time spent in the current city (by year) and marital status (married or unmarried), as well as the number of three kinds of goods purchased by customers and the final amount spent.

From this table, I want to know the number of goods purchased in three categories under different categories. For example, according to gender, we observed the purchase of the three commodities by male and female.

At the same time, I also want to know the consumption power of different categories, that is, the amount spent. For example, by age, observe which age group has the strongest purchasing power, and what is its proportion in the total consumption.

What's more, we should combine the various categories, such as observing the purchasing power of men and women of different ages in different city levels, so as to carry out a more specific control.

Finally, you can also get the cost of each user through the table, rank according to the cost, select the shopping star of Black Friday, and display it.

### Characteristics

This data set is very large, with more than 570000 pieces of data. There are many items in the dataset, including age, gender, occupation, city, time of living in the city, marital status, user ID, commodity ID, commodity category, total consumption.I think we should pay more attention to the relationship between user information and sales volume and total consumption of various commodity categories.

​	The characteristics of all the attributes I used are list here:

#### User_ID

According to statistics, 5861 different users are included in 570000 pieces of data_ ID, in the last shopping star show, I selected the top ten users with the highest consumption amount to show their ID and consumption amount.

#### Gender

In the data set, the number of men and women is basically the same.

#### Age

The age groups in the dataset are divided into 8 age groups, which are 0-17, 18-25, 26-35, 36-45, 46-50, 51-55 and 55 +.

#### Occupation

The occupations in the data set are displayed by numerical numbers. I don't know what occupation each number represents, so I can only use numerical numbers in the chart display. There are 20 occupations.

#### City_Category

The cities in the data set are classified into three categories: A, B and C. There is no relevant data to show that the grade of a is higher than that of B and C.

#### Stay_In_Current_City_Years

There is a column of data in the data set, which is "year of living in the city", divided into 0, 1, 2, 3 and 4 +.

#### Marital_Status

The marital status in the dataset is divided into 0 and 1. I think 0 stands for unmarried and 1 stands for married.

+++++++++++

For the above classification, I use the drop-down options to update the chart, as shown in the figure below.

![](https://dzy-typora-img-hosting-service.oss-cn-shanghai.aliyuncs.com/typoraImgs/HCI-Lab3-01.png)

#### Product_Category

There are three commodity categories in the dataset, which are product_ Category_ 1，Product_ Category_ 2，Product_ Category_ 3。 The sales volume of each commodity category is displayed.

I chose the multi column bar chart to show the three commodity categories.

![image-20210624153053919](https://dzy-typora-img-hosting-service.oss-cn-shanghai.aliyuncs.com/typoraImgs/HCI-Lab3-02.png)

![image-20210624153215636](https://dzy-typora-img-hosting-service.oss-cn-shanghai.aliyuncs.com/typoraImgs/HCI-Lab3-03.png)



## Interact Between User & Dashboard

GIF can see in the .md.

#### Switch from different item in the category

![dropdown-category](https://dzy-typora-img-hosting-service.oss-cn-shanghai.aliyuncs.com/typoraImgs/HCI-Lab3-04.gif)

#### Sunburst to show thespecific composition of data

![sunburst](https://dzy-typora-img-hosting-service.oss-cn-shanghai.aliyuncs.com/typoraImgs/HCI-Lab3-05.gif)

#### Double-dropdown-select

![double-dropdown](https://dzy-typora-img-hosting-service.oss-cn-shanghai.aliyuncs.com/typoraImgs/HCI-Lab3-06.gif)

#### Table slide around

![table-slide](https://dzy-typora-img-hosting-service.oss-cn-shanghai.aliyuncs.com/typoraImgs/HCI-Lab3-11.gif)



## Layout of Designed Dashboard

- After I finish the **Data Analysis Task**, I have an ideal overview of this database, and then I concentrate more on the design of the **Data Visualization**.

  ![image-20210624155114125](https://dzy-typora-img-hosting-service.oss-cn-shanghai.aliyuncs.com/typoraImgs/HCI-Lab3-07.png)

  ​	I used one of the layouts recommended by the teacher. The page has a title at the head. The following is the introduction of the data set. Then there is a bar chart. In the middle, a row of pie chart and sunrise chart are juxtaposed. Finally, there is a table.

  ![](https://dzy-typora-img-hosting-service.oss-cn-shanghai.aliyuncs.com/typoraImgs/HCI.png)

  ![image-20210624160914874](https://dzy-typora-img-hosting-service.oss-cn-shanghai.aliyuncs.com/typoraImgs/HCI-Lab3=09.png)

  ![image-20210624160936156](https://dzy-typora-img-hosting-service.oss-cn-shanghai.aliyuncs.com/typoraImgs/HCI-Lab3-10.png)

## Patterns Revealed in the Figures

- I draw 4 graphs for this data set:

  1. Grouped Bar Chart

     ![image-20210624163423954](https://dzy-typora-img-hosting-service.oss-cn-shanghai.aliyuncs.com/typoraImgs/HCI-Lab3-12.png)

     ```python
      'data': [
                 go.Bar(name='Product_Category_1', x=y_name, y=group_result['Product_Category_1'][y_name]),
                 go.Bar(name='Product_Category_2', x=y_name, y=group_result['Product_Category_2'][y_name]),
                 go.Bar(name='Product_Category_3', x=y_name, y=group_result['Product_Category_3'][y_name])
             ],
             'layout':
                 go.Layout(
                     xaxis={
                         'title': category,
                     },
                     yaxis={
                         'title': 'Sales',
                     }
                 )
     ```

  2. Sunburst of a rectangular DataFrame

     ![image-20210624164024922](https://dzy-typora-img-hosting-service.oss-cn-shanghai.aliyuncs.com/typoraImgs/HCI-Lab3-13.png)

     ```python
      fig = px.sunburst(file, path=['City_Category', 'Gender', 'Age'], 	values='Purchase_Percent')
     ```

  3. Content-rating-Pie Chart

     ![image-20210624164153981](https://dzy-typora-img-hosting-service.oss-cn-shanghai.aliyuncs.com/typoraImgs/HCI-Lab3-14.png)

     ```python
         if values == "Product_Category_1_Sales":
             values = "Product_Category_1"
         elif values == "Product_Category_2_Sales":
             values = "Product_Category_2"
         elif values == "Product_Category_3_Sales":
             values = "Product_Category_3"
     
         fig = px.pie(file, values=values, names=names)
     ```

  4. Dash Table

     ![image-20210624164246771](https://dzy-typora-img-hosting-service.oss-cn-shanghai.aliyuncs.com/typoraImgs/HCI-Lab3-15.png)

     ```python
         fig = go.Figure(data=[go.Table(
             header=dict(values=['User ID', 'Total Cost']),
             cells=dict(values=[id, rank]))])
     ```

- About the **Bar chart**:

  - From the perspective of gender, the number of three kinds of goods purchased by women is much larger than that of men. Men and women buy the second kind of goods the most, followed by the first kind of goods, and the third kind of goods the least.
  - In terms of age, people aged 26-35 buy the most goods, while people aged 0-17 buy the least.
  - From the perspective of occupation, people with occupation number 4 buy the most goods, while people with occupation number 8 buy the least goods.
  - From the perspective of city level, people in B-class cities buy the most goods.
  - From the time of living in the city, people who live in the city for one year buy the most goods.

- About the **Sunburst**:

  - In the actual project, the use of sunrise chart can further subdivide the traceability analysis data, and truly understand the specific composition of the data.
  - In every level of city, women buy more than men. Both men and women, 26-35 years old people buy the most.

- The *Content Rating* **Pie Graph**:

  - Female consumption accounted for 76.8% of the total
  - The 26-35 age group accounted for 39.9% of the total consumption, while the 0-17 age group accounted for only 2.64%
  - The ratio of unmarried sales to married sales is about 6:4

- The **Dash Table**

  - The number 1004277 has become a shopping star, with a total cost of 10536783.
