name: Bug report
description: Create a bug report for an encountered issue.
title: "[BUG] "
type: bug
assignees: ''
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report
  - type: textarea
    attributes:
      label: Bug Description
      description: A clear and concise description of what the bug is.
    validations:
      required: true
  - type: textarea
    attributes:
      label: Steps to Reproduce
      description: Provide step-by-step instructions on how to reproduce the bug.
      placeholder: |
      1.
      2.
      3.
  - type: textarea
    attributes:
      label: Expected behavior
      description: A clear and concise description of what you expected to happen.
    validations:
      required: true
  - type: dropdown
    id: Reproducible
    attributes:
      label: Is this bug reproducible?
      description: How severe is this bug?
      options:
        - Yes
        - Sometimes
        - No
    validations:
      required: true
  - type: textarea
    attributes:
      label: Screenshots
      description: If applicable, add screenshots to help explain your problem.
    validations:
      required: false
  - type: textarea
    attributes:
      label: Test Environment
      placeholder: |
      - Machine: 
      - Build: 
      - SDK build: 
  - type: input
    id: contact
    attributes:
      label: Who found and reported this bug
      description: Use your github handle
      placeholder: ex. email@example.com
    validations:
      required: true
  - type: textarea
    attributes:
      label: Additional context
      description: Add any other context about the bug here.
