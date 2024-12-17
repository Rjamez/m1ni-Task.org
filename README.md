# Task Manager CLI

==================

# Description

This is where i Create a Task Manager CLI application that allows users to efficiently manage their tasks through a user-friendly command-line interface. The application will support CRUD (Create, Read, Update, Delete) operations for tasks, allowing users to organize and prioritize their work effortlessly.

# Problem Statement

The application should be able to handle the following scenarios:

-Managing tasks manually can become cumbersome and inefficient, especially as the number of tasks grows. Many individuals rely on simple to-do lists, which can lead to:

- Data redundancy and errors: Manual entries often result in duplications or mistakes.
- Difficulty in tracking progress: Hard to identify which tasks are completed or still pending.
- Limited ability to search, update, or organize information: Basic lists lack functionality for categorization or filtering.
- Lack of organization: Without a structured system, it’s easy to overlook important deadlines or priorities.

# Proposed Solution

To Develop a CRUD-based Task Manager CLI that allows users to efficiently manage their tasks. The system will provide:
Structured Task Management: Centralized management of tasks with clear attributes, such as due dates and priorities.
CRUD Operations: Easy-to-use functions for creating, viewing, updating, and deleting tasks.
Task Filtering and Sorting: Users can filter tasks by status (completed/incomplete) and sort them by due date or priority.
Persistence: Store tasks in a database (like SQLite) or a JSON file to retain data between sessions.
Ease of Use: An intuitive command-line interface that guides users through their task management activities.

# Table Relationships

For this simplistic model, we may not have complex relationships, but we could define a straightforward structure:
Tasks:
Attributes:
id (Primary Key)
title (String)
description (String)
due_date (Date)
priority (String: Low, Medium, High)
status (Boolean: Completed or Incomplete)

# User Stories

Task Management:
-Add: Users can add a new task by providing a title, description, due date, and priority.
-View: Users can view a list of all tasks, showing their details including the status, due date, and priority.
-Update: Users can update the details of an existing task, changing attributes like title, description, or status.
-Delete: Users can delete a task from their list by its ID.
Task Filtering and Sorting:
-Filter: Users can view tasks based on their completion status (e.g., all, completed, incomplete).
-Sort: Users can sort tasks by due date or priority to better manage their workload.
Persistent Storage:
-Users can save their tasks in a local database or file so that tasks persist across sessions.
-Users should be able to load tasks when starting the application and save their changes.

Copyright (c) 2024 [Robin James]
==========================================================================================
