### HTTP接口文档

0. 获取文章 - **GET** `/api/articles/`

   开发者: Roctey

   版本号: v1

   接口说明: 获取当前所有文章

   使用帮助: 暂无

   请求参数:

   | 参数名   | 类型   | 是否必填 | 参数位置 | 说明   |
   | -------- | ------ | -------- | -------- | ------ |
   | count    | 整数   | 否       | 查询参数 | 总数   |
   | next     | 字符串 | 否       | 查询参数 | 下一页 |
   | previous | 字符串 | 否       | 查询参数 | 上一页 |
   | results  | list   | 否       | 查询参数 | 结果   |

   响应信息:

   ```Python
   
   {
       "count": 2,
       "next": null,
       "previous": null,
       "results": [
           {
               "articleid": 1,
               "title": "First article",
               "author": "Roctey",
               "describe": "测试部的人都很帅",
               "content": "测试部的人真的都特别帅",
               "created_time": "2020-03-18T18:00:41.507331+08:00",
               "last_update_time": "2020-03-18T18:00:41.507331+08:00",
               "tag": []
           },
           {
               "articleid": 2,
               "title": "Second article",
               "author": "Roctey",
               "describe": "测试部的人都很帅",
               "content": "测试部的人真的都特别帅",
               "created_time": "2020-03-19T11:42:41.608805+08:00",
               "last_update_time": "2020-03-19T11:42:41.608805+08:00",
               "tag": []
           }
       ]
   }
   ```

1. 添加文章 - **POST** `/api/articles/`

   开发者: Roctey

   版本号: v1

   接口说明: 添加文章

   使用帮助: 暂无

   请求参数:

   | 参数名   | 类型   | 是否必填 | 参数位置 | 说明 |
   | -------- | ------ | -------- | -------- | ---- |
   | title    | 字符串 | 是       | 消息体   | 标题 |
   | author   | 字符串 | 是       | 消息体   | 作者 |
   | describe | 字符串 | 是       | 消息体   | 描述 |
   | content  | 字符串 | 是       | 消息体   | 内容 |

   响应信息:

   - 新增成功 - 状态码**201**:

     ```python
     {
         "articleid": 3,
         "title": "Third article",
         "author": "Roctey",
         "describe": "The people in the module testing department are very handsome",
         "content": "The people in the module testing department are very handsome",
         "created_time": "2020-03-19T13:48:45.540721+08:00",
         "last_update_time": "2020-03-19T13:48:45.540721+08:00",
         "tag": []
     }
     ```

   - 必填字段为空 - 状态码**400**:

     ```python
     {
         "title": [
             "该字段不能为空。"
         ],
         "author": [
             "该字段不能为空。"
         ],
         "describe": [
             "该字段不能为空。"
         ]
     }
     ```

2. 编辑文章 - **PUT** `/api/articles/{文章编号}/`

   开发者: Roctey

   版本号: v1

   接口说明: 添加文章

   使用帮助: 暂无

   请求参数:

   | 参数名   | 类型   | 是否必填 | 参数位置 | 说明 |
   | -------- | ------ | -------- | -------- | ---- |
   | title    | 字符串 | 是       | 消息体   | 标题 |
   | author   | 字符串 | 是       | 消息体   | 作者 |
   | describe | 字符串 | 是       | 消息体   | 描述 |
   | content  | 字符串 | 是       | 消息体   | 内容 |

   响应信息:

   - 编辑成功 - 状态码**200**:

     ```python
     {
         "articleid": 9,
         "title": "Sixth article",
         "author": "Roctey",
         "describe": "test article",
         "content": "So Beautiful Lie.",
         "created_time": "2019-11-04T12:27:55.614420+08:00",
         "last_update_time": "2019-11-04T12:27:55.614481+08:00",
         "tag": []
     }
     ```

   - 编辑失败 - 状态码  同添加文章

3. 删除文章 - **DELETE** `/api/articles/{文章编号}/`

   开发者: Roctey

   版本号: v1

   接口说明: 添加文章

   使用帮助: 暂无

   请求参数:

   | 参数名   | 类型   | 是否必填 | 参数位置 | 说明   |
   | -------- | ------ | -------- | -------- | ------ |
   | count    | 整数   | 否       | 查询参数 | 总数   |
   | next     | 字符串 | 否       | 查询参数 | 下一页 |
   | previous | 字符串 | 否       | 查询参数 | 上一页 |
   | results  | list   | 否       | 查询参数 | 结果   |

   响应信息:

   - 删除成功 - 状态码**200**:
   - 删除成功 - 状态码**404**:

