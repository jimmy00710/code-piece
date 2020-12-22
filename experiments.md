# Experiment Logs 

## Intro - 
This file will act as a log book in which I will write everystep which I have taken while conducting this experiment. So I am building a resume filter. The thing is I was getting a lot of resumes when I am doing the work. It takes around 1-2 hours to go through 100 resumes and it breaks my link also. So for this reason I thought to build a resume filter.<br>

In this we will experiment different classification algorithm, NLP preprocessing, RNN, LSTM and at last BERT. 

## PyScripts
## 
So till now I have written 2 py files one is for scanning the whole directory and returning me the list of all the resumes pdfs.<br>
Next I have written a pyscript for converting all those pdfs into text and created a another pyscript name csvcreate to create a csv name<b><i> content.csv </i></b> in the data/csv folder. This csv contains 2 columns. The column names are as follows :- 
> content <br>
> labels <br>

The content holds the text data and the label holds the selected and not selected data. The selected candidates are marked as 1 and not selected candidates are marked as 0. <br>
In total there are <b>176</b> resumes. Out of which <b> 120 </b> are not selected and only <b> 56 </b> are selected. <br>

Now since our data is in the csv we can start with the preprocessing. 
<br>
<br>
## Preprocessing
So before applying any sort of preprocessing let us see what is there in the resume data - 
> Names <br>
> Location <br>
> Mobile Number <br> 
> Email ID <br>
> Achievements <br>
> Projects <br>
> Experience <br>
> Qualifications<br>

So out of these things we don't need Names,Location, Mobile Number and Email Id. The reason we don't need name and location is because of the bias factor. In case if we have selected 5 abhishek name person the classifier can learn that we are prefering the abhishek person. Other than these 2 the mobile number and email ID are just the noise which we can avoid. <br>

The reason why I am not doing lowercasing first is because in the resume some people can use AI as the term and I don't want those abbrevation to change into ai, so before lowercasing I will use the expansion mechanism. After that we will lowercase the text.<br>

### Challenge in Preprocessing the Data
So the first challenge I faced was how to remove the names, address, mobile number and email id. <br>
I mean how to remove these things. The most challenging thing is to remove the name of the person. Since we don't know or we don't have the person name in the resume it is very tricky to take out those names. <br>
One approach which I thought of was that in 80% resume we see the name in top row. So what I did was using <b>NER</b>
I find the first word which has the <b> PERSON </b> tag and remove it. 80% cases we were able to find the name at the top. In some case I was able to find the email id or some online profile, or some type of punctuation.  I am thinking of writing a function to remove these punctuations and the online profile and then look for the name. <br>
The next approach which I am thinking is to use wordnet and add some other words which I see in data science field. Other than these words which will come will be most probably names, address, phone number or something or the other. <br>
> Should we remove the number from the resume ?? <br>
> I think we should remove the numbers as they don't play any major role. I am not looking for there percentage. 
I am looking there project work.<br>

I am thinking of using set of algorithms on 2 things one with Names and Address and the other without names,
and addresses.

## Finding Names From the Resumes - 
* So earlier I tried using Spacy NER large model and with that all the word which have person tag we were filtering that. But the problem with that was some common words were also getting filtered. So we needed a corpuse of words which were commonly used and we can check if those words comes or not. For this corpus of words I used <b> wordnet. </b> Wordnet has a large corpus of words which are commonly used and since those are english words( it so happened that the resumes i am shortlisting are indian resumes so those names are not in wordnet and even there address.) Using these 2 I got almost all the names, but along with them I was also picking data science terms. So to resolve that I kept a list of common words which occur in data science ( tensorflow, pytorch, keras, h2o, knn etc) and checked that if these words come then we can no need to filter them out. Although this process takes some analysis on what word is coming but it I think it is a great way to fetch the unique names and words from the data. 

<br>
<br>

## LogBookName -
The log book name is experiment. Once I do that I will create a pycscript for it and thats it For now. <br>


<br>

## Tutorial
<a href="https://towardsdatascience.com/machine-learning-text-processing-1d5a2d638958"> Machine Learning Text Processing </a> <br> 

<a href=https://www.kdnuggets.com/2019/01/solve-90-nlp-problems-step-by-step-guide.html> NLP Problem step by step Guide </a> <br>


## Ingredients for Building Classification Model
> words_frequency <br>
> wordcloud for visualization <br>
> Converting the word to vector (Glove, Word2vec, TfIdf) <br>
> Runnig our algorithms (Naive Bayes, SVM, Logistic Regrssion)
