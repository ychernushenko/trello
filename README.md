# trello
Simple trello version. Create Trello Web Application

##Requirements
1. Allow edit/create/delete Status entity in the admin page
1.1. Status has only one field - name
1.2. Name value could be only one of (New/InProgress/OnReview/Tested/Delivered)
1.3. Names should be unique. If user try's to create Status that already exists he should get an error - "Данный статус уже существует" (RUS - "This status already exists")

2. In Admin page you can edit/create/delete Task entity
2.1. Task has field name, which can not be empty
2.2. Task has field status, which can be only one of the existing statuses

3. Applications should display Statuses with corresponding tasks 
3.1. All statuses and tasks should be displayed on one page

4. Application should allow to change tasks statuses by drag-and-drop
4.1. Changes on DOM should not reload the whole page, only specific elements 

Application should be developed on Python 2.7 using Django framework. No restrictions on front-end frameworks.
