**T15 Gnosis official submission for CP-03 in the course IT496**

We were alloted 3 tasks, in Task 1 we had to show our creativity, in that we are predicting number of extras as well as number of boundaries scored in the final of ICC world cup 2023 which is going to take place in Narendra Modi Stadium, Ahmedabad. In Task 2 we had to predict the 2 finalists and their playing 11, in the final task which is Task 3 we have to predict the winner of ICC world cup 2023.

**Our Official website to predict result between any 2 teams built using Flask API**
[Website](https://t15-gnosis-cp3.onrender.com/)

**Our Predictions are as follows:**
1) Number of boundaries in final match : 30 when Team India bats and 31 when South Africa bats <br>
2) Number of extras in final match : 21 Runs <br>
3) Finals Prediction: India vs South Africa <br>
4) Winner of ICC World Cup 2023: India <br>

**Playing 11 for India :**
Rohit Sharma, Shubman Gill, Virat Kohli, Shreyas Iyer, KL Rahul, Ravindra Jadeja, Jasprit Bumrah, Mohammed Siraj, Mohammed Shami,Kuldeep Yadav and Suryakumar Yadav <br>

**Playing 11 for South Africa :** 
Temba Bavuma, Aidam Markram, David Miller, Rassie Van der Dussen,Heinrich Klassen, Quinton de Kock,Keshav Maharaj, Kagiso Rabada, Lungi Ngidi,Gerald Coeztee,Marco Janson



In order to perform all of these tasks we have used multiple datasets which were available in the public domain through [link1](https://www.kaggle.com/code/bhuvaneshprasad/sample-notebook-for-odi-matches-data) and [link2](https://www.kaggle.com/datasets/pardeep19singh/icc-mens-world-cup-2023). Apart from this we have used several classical Machine Learning models and used Artificial Neural Networks as well. In our main file you will find the entire flow of our project but to see the contribution of every team member you can check their own .ipynb files. (Commit history is also well maintained)

We have also added an extra layer in order to make it truely end-to-end, and deployed a website made through Flask API which uses this model and lets user enter any two teams with the Match Venue and it will predict who will win. Front-end of this webpage is done through html/css and it is deployed on[render.com](http://render.com/)

Note: The input features used for tasks 1,2,3 is different in compared to that of website, this is done to maintain the simplicity of the webpage. As we are using a free account on render, the servers will spin up after visiting the page which makes the load time to be 2-3 seconds so be patient with it.
