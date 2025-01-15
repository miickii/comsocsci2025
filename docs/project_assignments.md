---
layout: page
title: project assignments
tagline: DTU 02467 Computational Social Science Course Spring 2024
description: A course led by Laura Alessandretti on Computational Social Science
---

 <div class="navbar">
     <div class="navbar-inner">
         <ul class="nav">
             <li><a href="#timeline">timeline</a></li>
             <li><a href="#groups">groups</a></li>
	     <li><a href="#preparation">preparation</a></li>
             <li><a href="#project_assignment">overview</a></li>
             <li><a href="#project_assignmentA">project assignment A</a></li>
             <li><a href="#project-assignmentB">project assignment B</a></li>
             <li><a href="#evaluation">evaluation</a></li>
         </ul>
     </div>
 </div>



### <a name="timeline"></a>Timeline


_Project Assignment A_  
Slides Due: Tuesday, Apr 16th, 23:59
Presentation: Wednesday, Apr 19th (in class)

_Project Assignment B_  
Due: Friday, May 10th, 23:59  


### <a name="groups"></a>Groups
* Assignments should be handed in in groups.
* You shall register in a group on DTU Learn. 
* Groups should have 3 members.
* You shall work in the same groups throughout the course.
* All group members should be familiar with every aspect of the assignment. Everyone in the group should be able to solve every exercise.
* It is possible to have fewer than 3 group members, but we judge all reports the same. 


### <a name="preparation"></a>Preparation
* During classes 9, 10, 11 and 12, you work independently to prepare Project Assignments A and B
* During classes 9 and 10, each group will have a 15 minutes meeting with the teacher, where we discuss your project idea, and you get  feedback
* I will contact each group via DTU Learn to set up the time and location (either in class or via Teams)
* Participation in the meeting is not mandatory. If you wish to opt out, please let me know in advance. 

### <a name="project-assignment"></a>Project Assignment Overview

The point of the Project Assignments is to try out the skills you've learned in the course on your own dataset. We've been working on understanding networks and text analysis, so the idea is to find a dataset to analyze that will let you show off what you can do with the tools you have learned.

Here are some examples of sources that you can consider using:

* [The list of APIs that you have put together](https://laura.alessandretti.com/comsocsci2024/survey_results_2.html). This is the list of APIS that you have collaborately developed. I added some comments. 
* [Standford Large Networks Dataset Collection](https://snap.stanford.edu/data/) is a collection of large network datasets.
* [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page) You can collect Wikipedia data for whatever you are into.
* You can also use data from specialized wikis (examples include [Wookiepedia](https://starwars.fandom.com/wiki/Main_Page), [Game of Thrones Wiki](https://gameofthrones.fandom.com/wiki/Game_of_Thrones_Wiki), [Simpson's Wiki](https://simpsons.fandom.com/wiki/Simpsons_Wiki), etc)
* [Netzschleuder](https://networks.skewed.de/). Another collection of Network Datasets.
* [Social Networks Awesome datasets](https://github.com/awesomedata/awesome-public-datasets#socialnetworks). Another collection of public social network datasets.
* Many social media (Twitter, Reddit, etc) have closed their APIS but you can find data archives online e.g. [Tweetsets](https://tweetsets.library.gwu.edu/datasets), [SOMAR](https://socialmediaarchive.org/?ln=en), [DocNow Catalog](https://catalog.docnow.io/),

Combining datasets is highly encouraged. This is a great way to learn new things (e.g. how the weather impacts network structures on Reddit or something).
And new ideas for datasets are very welcome. You should work with something that interests you - that way the project will be much more fun to work on. You will be working together in groups just as for the first two assignments.


### <a name="project-assignmentA"></a> Project Assignment A

For the initial part of your final project, you shall create a 5-minute presentation. The presentation shall outline the core concept of your project, the datasets involved, and your methodology. You're making the presentation so that I can give you feedback, and you can get ideas from other groups.    

#### Requirements     

The presentation must contain the following:    

- **Central Idea & Data**
  - *Project Idea*: What is the central idea of your project? Explain your objective and what makes your project interesting. 
  - *Data Acquisition*: Describe the datasets required for your project. Detail the process of how these datasets were obtained, including any relevant sources or methods used for downloading.
  
- **Project Framework and Implementation Plan**
  - Provide an outline on the elements you'll need to get to your goal & the implementation plan.

- **Preliminary Data Analysis Overview**
  - *Data Size*: Quantify the total size of your dataset (in megabytes, number of rows, variables, etc.).
  - *Network Analysis*: Describe the basic properties of the network you will analyze (e.g., number of nodes, links, degree distributions)? 
  - *Textual Data Examination*: Discuss the textual elements within your dataset and your approach to analyzing this content.
  - *Text/Network integration*: Explain how you intend to integrate the network and textual data analyses to draw comprehensive insights.

#### Practicalities
Here are some details about the format and submission of your presentation. 
- *Presentation Format*: There are no stringent format requirements for the presentation, but you will be asked to stay within 5 minutes. 
- *Audience*: The presentation will be delivered to the entire class.
- *Platform*: Submit your presentation slides on DTU Learn.
- *Deadline*: Given the extensive data work involved, you will have 2 weeks to prepare and submit your slides.


### <a name="project-assignmentB"></a> Project Assignment B.

The deliverables for the final project will be

__A website__. The website should contain the result of your analysis, it should tell the story about the data that you're interested in getting across. The website should not be technical, but rather aim at using visualization and explanation to get your insights across to a non-scientific reader.

__An explainer Notebook__. The Notebook should contain all the behind the scenes, details on the dataset, why you've selected this particular dataset, explanations of your choices regarding network analysis, etc. You should link to the notebook from the website. Make sure that the notebook is formatted according to the formatting rules detailed below. 


#### More about the website

The main point of the website is to present your idea/analyses to the world in a way that showcases your use of what you've learned in class. It can be as simple as an old fashioned static web-page, and as complicated as you want it to be. Let your creativity run wild. However, keep in mind that this is not a website coding class - I care only about content and analysis (more in the Evaluation section below). 

The website should be self-contained and tell the story of your dataset without the need for the Explainer Notebook (the purpose of the notebook is to provide additional details for interested readers). Here are some requirements: 

* The page should say clearly what the dataset is and give the reader some idea of its most important properties (kind of Project Assignment A-style).
* The website can contain a maximum of 5 figures. 
* Text should be clear and concise. 
* The page should contain the result of your network and text analysis (that's the main part).
* There should be download options for data sets (so the user can play around).
* You must link to the Explainer Notebook (more details below) that explains the details of your analysis (including all of the machine learning, the model selection, etc). You can achieve this with a link to a notebook displaying on the nbviewer.
* For hosting, I recommend using your DTU website or Github pages.


#### More on the explainer notebook

##### Content 
The notebook should contain your analysis and code. Please structure it into the following 4 sections

1. Motivation
    * What is your dataset?
    * Why did you choose this/these particular dataset(s)?
    * What was your goal for the end user's experience?
2. Basic stats. Let's understand the dataset better
    * Write about your choices in data cleaning and preprocessing
    * Write a short section that discusses the dataset stats (here you can recycle the work you did for Project Assignment A)
3. Tools, theory and analysis. Describe the process of theory to insight
    * Talk about how you've worked with text, including regular expressions, unicode, etc.
    * Describe which network science tools and data analysis strategies you've used, how those network science measures work, and why the tools you've chosen are right for the problem you're solving.
    * How did you use the tools to understand your dataset?
4. Discussion. Think critically about your creation
    * What went well?
    * What is still missing? What could be improved? Why?


##### Formatting 

- *Divide Your Notebook*: Do not make all the anlaysis in a single code cell. Structure your code in different sections. Give a title to each part to make it clear what the section is about. 
- *Conciseness*: Write clear and concise text.
- *Code Documentation and Output formatting*: Include all necessary code and ensure it is well-documented and tidy. Avoid lengthy outputs and ensure there are no errors displayed.
- *Plot Formatting*: Format your plots properly. Label axes on plots and include explanatory text. 
- *Use of References*: Cite references appropriately following academic standards.
- *Objective Language*: Be precise, write in objective language (avoid: "I think ...", "In my opinion...", etc) - if you make an observation, support it with data.


### <a name="evaluation"></a> Evaluation.    

Your project assignment will be assessed based on the following. The evaluation is based on the assessment of Part A and Part B. 

- **Overall project quality**
	- *Motivation is clear.* The project's purpose and significance are well explained and sound. 
	- *Dataset is appropriate.* The chosen dataset(s) are relevant to the project's objectives. 

- **Explainer notebook**
	- *Data collection and pre-processing.* Choices made during data collection and pre-processing are clearly presented and sound.
	- *Discussion.* The notebook presents sound reflections on the findings.
	- *Formatting.* The notebook is well-organized and formatted for readability.

- **Use of network science**
	- *Appropriate strategies.* Techniques and methods used are suitable for the project's goals.
	- *Comprehensiveness.* The analysis covers all necessary aspects of the network analysis.
	- *Correctness.* Conclusions drawn from the data are valid and supported by the network analysis.
	
- **Use of text analysis tools**
	- *Appropriate strategies.* Methods are effectively chosen to meet the project objectives. 
	- *Comprehensiveness.* The project explores all the necessary aspects of the textual component.
	- *Correctness.* Conclusions drawn from the data are valid and supported by the text analysis.
	
- **Website Formatting**
    - *Curated visualizations*. Figures are designed according to fundamental principles of visualization to ensure high quality. Figures enhance the project's narrative and provide clear insights.
	- *Clear explanations.* The website clearly and concisely articulates the project's motivation, data background, findings and discussions.
    - *Usability*: The website is user-friendly, with a logical structure that facilitates understanding of the analysis.

- **Additional Criteria**
    - *Innovation, Creativity and Challenge*: Projects demonstrate originality and/or present challenges in relation to one or several of the following aspects: idea formulation, data collection, network analysis, text analysis, presentation. 
    - *Ethical Considerations*: Projects discusses and/or addresses appropriately ethical aspects related to data use, biases, and privacy. 

**Scoring:** Scores are assigned for each criterion on a scale from 0 (insufficient), 1 (sufficient), 2 (good) to 3 (excellent), with the possibility of half-point increments (e.g., 0.5, 1.5, 2.5). The overall evaluation is the average of these scores.

