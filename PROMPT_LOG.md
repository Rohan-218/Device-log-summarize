# PROMPT_LOG.md

## 1. Understanding the Project

**Prompt I used:**

"I got an assessment to build a Device Log Summarizer CLI tool. Can you explain what this tool actually does and what I need to build for this assessment?"

**How AI helped:**

I was not familiar with the term Device Log Summarizer CLI tool, so I asked AI to explain the concept and the assessment requirements in simple words. This helped me understand the expected workflow, including reading CSV data, calculating device statistics, exporting JSON, and generating a chart.

## 2. Cleaning Sensor Readings

**Prompt I used:**

"What is a good way to clean a list of sensor readings containing strings, None values, negative numbers, and values above 500? How should I handle empty lists and test these cases?"

**How AI helped:**

AI helped me understand the different edge cases and how type conversion, filtering, and clipping should work. I used this guidance while working on the cleaning function and wrote test cases to check its behavior.

## 3. Reading CSV and Creating JSON

**Prompt I used:**

"How can I group CSV records by device_id and calculate the record count, average temperature, and number of ERROR records? Also, how should I filter devices with an average temperature above 80 and save the results in JSON?"

**How AI helped:**

I used AI to clarify the data processing steps and understand how to calculate the required statistics. It also helped me think about handling missing files, invalid temperature values, and CSV columns that might be missing.

## 4. Creating the Bar Chart

**Initial prompt I used:**

"How can I use Matplotlib to read my JSON output and create a bar chart comparing the average temperature of each device? I also need a title, axis labels, and a PNG output file."

**Issue noticed during review:**

I considered the possibility of device labels overlapping or getting cut off, especially when the device IDs are long.

**Follow-up prompt I used:**

"How can I improve the chart layout so the device labels are easier to read? Explain how rotating the x-axis labels and using tight_layout() can help."

**How AI helped:**

AI helped me understand the Matplotlib formatting options and how to improve the chart's readability. I used these suggestions to review the layout and make the chart easier to understand.

## 5. Testing and Fixing Issues

**Prompt I used:**

"What happens if the CSV file is missing or the file path is incorrect? How can I handle this error so the program displays a proper message instead of crashing?"

**How AI helped:**

AI explained how to handle `FileNotFoundError` using a `try-except` block. This helped me understand how to handle missing input files and display a meaningful error message to the user.

## 6. Creating the Prompt Log

**Prompt I used:**

"Compile my earlier prompts about this project and use the text from the attached file to summarize how AI helped me during development. Keep the language simple and natural, and include the main questions I asked, the issues I faced, and how I used the suggestions."

**How AI helped:**

AI helped me organize my interactions into a single document. I used it to summarize the areas where I sought guidance, including understanding the assessment, handling edge cases, troubleshooting testing issues, and improving the chart layout.

## 7. Final Notes

I mainly used AI to understand the requirements, clarify Python concepts, explore edge cases, and troubleshoot issues during development. I also used it to learn about Matplotlib formatting and improve the readability of the chart. I reviewed the suggestions and checked the results as I worked through the different parts of the assessment.