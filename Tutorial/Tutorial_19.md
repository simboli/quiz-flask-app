I apologize for the oversight. It seems that the `page_load_time` column is missing in the `session_info` table. To fix this issue, you need to add the `page_load_time` column to the `session_info` table. You can do this using an ALTER TABLE statement:

```sql
ALTER TABLE session_info
ADD page_load_time DATETIME;
```

After adding the `page_load_time` column to your `session_info` table, your code should work without any issues.