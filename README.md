# Markdown Timesheet

A command line interface to total up the time entries in a markdown file.

## Installation

```
pip install markdown_timesheet
```
## Usage

Given a `timesheet.md` like so:

```
# 5 Sep 2019

## 9:15-9:16, 9:20-9:25
Write spec, write client email.
  - wrote really basic spec
	- told client I'm starting the project

## 9:25-9:29
Write tests

```

Then,

```
$ add timesheet.md
10
```

