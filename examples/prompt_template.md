# Without Prompt Template:

### Input:
```
Tôi tên là Tú Phạm và tôi đang sống
```
### Output:
```
và làm việc tại Đà Nẵng.
```

# With Prompt Template:

```
Cuộc trò chuyện giữa một con người tò mò và một trợ lý trí tuệ nhân tạo.
Trợ lý AI nói nhiều và cung cấp nhiều chi tiết cụ thể từ ngữ cảnh của nó.

USER: 3 Màu sắc cơ bản là gì? 
ASSISTANT: 
```
### Output:
```
RGB là hệ màu được tạo nên từ 3 màu cơ bản bao gồm: màu đỏ, xanh lục và xanh lam.
```

# Zero Shot Template:

```
Cuộc trò chuyện giữa một con người tò mò và một trợ lý trí tuệ nhân tạo.
Trợ lý AI nói nhiều và cung cấp nhiều chi tiết cụ thể từ ngữ cảnh của nó.

USER: Thêm từ thích hợp vào câu sau: "Mặt trời mọc ở hướng _____ và lặn ở hướng Tây"
ASSISTANT: 
```
### Output:
```
Đông
```

# One Shot Template:

```
Cuộc trò chuyện giữa một con người tò mò và một trợ lý trí tuệ nhân tạo.
Trợ lý AI nói nhiều và cung cấp nhiều chi tiết cụ thể từ ngữ cảnh của nó.

USER: Chọn đáp án đúng. Loài động vật nào sống ở sa mạc?
A. Gấu
B. Lạc đà
C. Cáo
ASSISTANT: Lạc đà
USER: Chọn đáp án đúng. Thành phố nào là thủ đô Việt Nam?
A. Đà Nẵng.
B. Hồ Chí Minh
C. Hà Nội
ASSISTANT:
```
### Output:
```
Hà Nội
```

# Few Shot Template:

```
Cuộc trò chuyện giữa một con người tò mò và một trợ lý trí tuệ nhân tạo.
Trợ lý AI nói nhiều và cung cấp nhiều chi tiết cụ thể từ ngữ cảnh của nó.

USER: 1 + 1 bằng mấy?
ASSISTANT: 2
USER: 2 + 3 bằng mấy?
ASSISTANT: 5
USER: 12 + 3 bằng mấy?
ASSISTANT: 15
USER: 9 + 1 bằng mấy?
ASSISTANT: 10
USER: 100 + 1 bằng mấy?
ASSISTANT: 101
USER: 21 + 9 bằng mấy?
ASSISTANT:
```
### Output:
```
30
```


# Stanford Alpaca Template examples
Readmore: https://github.com/tatsu-lab/stanford_alpaca

### For examples with a non-empty input field:

```
Below is an instruction that describes a task, paired with an input that provides further context.
Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Input:
{input}

### Response:
```

### For examples with an empty input field:


```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:
```