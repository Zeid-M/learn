Writing better comments is an essential skill that enhances the readability, maintainability, and overall quality of your code. Good comments guide readers (including future you) through your thought process, clarify complex sections, and document important decisions. Below, I will guide you through some best practices, with examples, to help you master the art of writing useful comments.

### 1. **Focus on Explaining the 'Why'**
   - **Bad Comment Example:**
     ```python
     i = 0  # Set i to 0
     ```
     This comment adds no real value. It is obvious from the code itself.

   - **Good Comment Example:**
     ```python
     i = 0  # Initialize counter for retry attempts
     ```
     This comment explains **why** `i` is being set to `0`, which provides useful context for understanding the code's intent.

### 2. **Use Comments to Explain Complex Logic**
   If a piece of code involves complex calculations or logic that might not be immediately intuitive, explain it clearly.

   - **Bad Comment Example:**
     ```python
     discount = price - (price * discount_rate)  # Calculate discount
     ```
     This comment doesn’t add anything beyond what the code is already saying.

   - **Good Comment Example:**
     ```python
     # Calculate the final price after applying the discount rate.
     # Note: The discount rate is expected to be between 0 and 1.
     discount = price - (price * discount_rate)
     ```
     This comment explains the context (final price) and provides important details (expectations for the discount rate) that aren’t immediately obvious from the code itself.

### 3. **Avoid Redundant Comments**
   Only write comments when they add value beyond what the code itself makes obvious.

   - **Bad Example:**
     ```python
     count += 1  # Increment count by 1
     ```
     This is self-explanatory. No need for a comment.

   - **Good Example:**
     ```python
     count += 1  # Increase the counter to reflect the newly processed record
     ```
     Here, the comment explains **why** you’re incrementing `count`—it tells the reader what this increment actually represents.

### 4. **Document Important Decisions**
   Comments are useful for explaining why a certain approach was chosen, especially when it’s not immediately obvious or involves trade-offs.

   - **Example:**
     ```python
     # Using binary search for better performance as the list is sorted.
     def find_element(sorted_list, target):
         ...
     ```
     This type of comment provides context on **why** a specific algorithm or data structure is being used.

### 5. **Use TODO Comments for Future Improvements**
   If you need to add something later or want to remind yourself (or others) of potential improvements:

   ```python
   # TODO: Optimize this loop to reduce the time complexity from O(n^2) to O(n log n)
   for i in range(len(data)):
       ...
   ```
   This comment lets others know that the current implementation is not ideal and gives them direction if they are revisiting the code.

### 6. **Separate Different Kinds of Comments**
   There are two common types of comments: **block comments** and **inline comments**.

   - **Block Comments:** Use them to describe a section of code.
     ```python
     # Loop through each item in the list and count occurrences.
     # This helps to identify the most frequently appearing elements.
     for item in item_list:
         ...
     ```
   
   - **Inline Comments:** Use them on the same line as the code they’re describing, but only when necessary.
     ```python
     result = []  # Initialize an empty list to store valid results.
     ```

### 7. **Avoid "Noise" Comments**
   Don't add comments that restate the obvious.

   - **Bad Example:**
     ```python
     # Import the datetime module
     import datetime
     ```
   The code is clear enough without a comment.

   A better approach is to explain why a specific import is needed, if that’s useful:
   ```python
   import datetime  # Needed for parsing and formatting date strings consistently.
   ```

### 8. **Use Clear Language and Be Consistent**
   - **Be direct and concise**: Avoid using long or flowery language. Get to the point quickly.
   - **Use proper grammar and spelling**: Poor grammar can confuse readers or make the comments hard to understand.
   - **Maintain consistency**: Use the same style and vocabulary throughout the project. If you have multiple developers, consider creating a standard for comments.

   **Good Comment Example:**
   ```python
   # Fetch customer data from the database based on customer ID.
   # If the customer ID is invalid, return None.
   customer_data = fetch_customer_from_db(customer_id)
   ```

### 9. **Explain Assumptions and Expected Input/Output**
   When writing a function, you may have certain expectations for input values, edge cases, or conditions.

   **Example:**
   ```python
   def process_order(order_id):
       """
       Processes an order by its ID.

       Args:
           order_id (int): The unique identifier of the order. Assumes that the order ID is valid 
                           and exists in the database.

       Returns:
           bool: True if the order is successfully processed, False otherwise.
       """
   ```
   The comment here clearly explains the assumptions about `order_id`, which helps the user understand how to use the function properly.

### 10. **Use Comments to Explain Non-Obvious Performance Considerations**
   If a piece of code is written in a particular way for performance reasons, it’s important to document that.

   - **Example:**
     ```python
     # Pre-allocating the list size to improve performance by reducing reallocations
     result = [None] * len(data)
     ```

### 11. **Summarize Logical Blocks of Code**
   When you have multiple lines that collectively perform a specific task, it helps to summarize that task at the start of the block.

   **Example:**
   ```python
   # Filtering out orders that are either invalid or have already been processed.
   valid_orders = []
   for order in all_orders:
       if order.is_valid() and not order.is_processed:
           valid_orders.append(order)
   ```

### Examples: Before and After
Consider the following code:

- **Before (Poor Comments):**
  ```python
  # Function to validate user
  def validate_user(user):
      if user.age > 18:
          return True
      else:
          return False
  ```

- **After (Better Comments):**
  ```python
  def validate_user(user):
      """
      Validates if the given user meets the age requirement.

      Args:
          user (User): An instance of the User class, containing user details.

      Returns:
          bool: True if the user's age is greater than 18, indicating they are an adult; otherwise False.
      """
      # Check if the user's age meets the minimum requirement to qualify as an adult
      return user.age > 18
  ```
  
### Recap: Guidelines for Writing Better Comments
1. **Explain the 'Why'**: Provide the reasoning behind the decisions.
2. **Avoid Stating the Obvious**: Don’t write comments that just repeat what the code does.
3. **Explain Complex Logic**: Clarify any algorithms, non-trivial calculations, or less obvious decisions.
4. **Be Concise and Clear**: Use simple, direct language.
5. **Maintain Relevance**: Ensure comments add value and update them when the code changes.
6. **Separate Concerns**: Use block and inline comments where they fit best.
7. **Document Important Assumptions**: Explain what you expect in terms of input/output.

When used effectively, comments provide invaluable insight, save time for future developers (including yourself), and make collaboration easier and more enjoyable. Practice writing thoughtful comments with these principles in mind, and over time you’ll develop a strong instinct for what’s needed.