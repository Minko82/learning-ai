# 🤖 **Learning AI**

## 📌 **Project Description**

A structured collection of notes, explanations, and tutorials covering the **basics of Artificial Intelligence**. 

<br>

---


## 📖 **Topics Covered**

Explore various AI concepts and techniques, including:

- 🎯 **Agents & Environments**: Definitions, percepts, states, rationality
- 🔍 **Search Algorithms**: BFS, DFS, Uniform Cost Search (UCS), Greedy Best-First Search, A* 
- 🏆 **Heuristic Search**: Admissibility, Consistency, and Heuristic Evaluation
- 📊 **Optimization & Problem Solving**: Constraint satisfaction problems, adversarial search
- 🤖 **Machine Learning Basics**
  
  
<br>

---

This repository is built upon concepts from renowned AI textbooks, online courses, and research papers, including:

- **MIT OpenCourseWare: Introduction to AI**
- Various academic papers on heuristic search and optimization


ttaching to medtronic-backend, medtronic-hand-tracker, medtronic-frontend
medtronic-backend | [2025-03-05 07:48:24 +0000] [1] [INFO] Starting gunicorn 23.0.0
medtronic-backend | [2025-03-05 07:48:24 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
medtronic-backend | [2025-03-05 07:48:24 +0000] [1] [INFO] Using worker: gevent
medtronic-backend | [2025-03-05 07:48:24 +0000] [20] [INFO] Booting worker with pid: 20
medtronic-backend | [2025-03-05 07:48:24 +0000] [21] [INFO] Booting worker with pid: 21
medtronic-backend | INFO:root:Flask Backend Starting...
medtronic-hand-tracker | ultraleap-hand-tracking-service: unrecognized service
medtronic-hand-tracker | ERROR:root:Failed to connect to shared memory: [Errno 2] No such file or directory: '/dev/shm/leapc_data'
medtronic-backend | INFO:root:Flask Backend Starting...
medtronic-hand-tracker | [ WARN:0@0.090] global cap_v4l.cpp:913 open VIDEOIO(V4L2:/dev/video0): can't open camera by index
medtronic-hand-tracker | [ERROR:0@0.090] global obsensor_uvc_stream_channel.cpp:158 getStreamChannelGroup Camera index out of range
medtronic-hand-tracker | [ WARN:0@0.090] global cap_v4l.cpp:913 open VIDEOIO(V4L2:/dev/video1): can't open camera by index
medtronic-hand-tracker | [ERROR:0@0.090] global obsensor_uvc_stream_channel.cpp:158 getStreamChannelGroup Camera index out of range
medtronic-hand-tracker | [ WARN:0@0.091] global cap_v4l.cpp:913 open VIDEOIO(V4L2:/dev/video2): can't open camera by index
medtronic-hand-tracker | [ERROR:0@0.091] global obsensor_uvc_stream_channel.cpp:158 getStreamChannelGroup Camera index out of range
medtronic-hand-tracker | [ WARN:0@0.091] global cap_v4l.cpp:913 open VIDEOIO(V4L2:/dev/video3): can't open camera by index
medtronic-hand-tracker | [ERROR:0@0.091] global obsensor_uvc_stream_channel.cpp:158 getStreamChannelGroup Camera index out of range
medtronic-hand-tracker | [ WARN:0@0.091] global cap_v4l.cpp:913 open VIDEOIO(V4L2:/dev/video4): can't open camera by index
medtronic-hand-tracker | [ERROR:0@0.091] global obsensor_uvc_stream_channel.cpp:158 getStreamChannelGroup Camera index out of range
medtronic-backend | INFO:root:GPU detected
medtronic-backend | INFO:root:GPU detected
medtronic-hand-tracker | ERROR:root:No valid hand tracking camera found.
medtronic-backend | INFO:root:Registered API Routes: Map([<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
medtronic-backend |  <Rule '/cpu' (HEAD, OPTIONS, GET) -> cpu_usage>,
medtronic-backend |  <Rule '/memory' (HEAD, OPTIONS, GET) -> memory_usage>,
medtronic-backend |  <Rule '/gpu' (HEAD, OPTIONS, GET) -> gpu_usage>])
medtronic-backend | INFO:root:Registered API Routes: Map([<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
medtronic-backend |  <Rule '/cpu' (HEAD, OPTIONS, GET) -> cpu_usage>,
medtronic-backend |  <Rule '/memory' (HEAD, OPTIONS, GET) -> memory_usage>,
medtronic-backend |  <Rule '/gpu' (HEAD, OPTIONS, GET) -> gpu_usage>])
medtronic-hand-tracker |  * Serving Flask app 'hand_tracker'
medtronic-hand-tracker |  * Debug mode: off
medtronic-hand-tracker | INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
medtronic-hand-tracker |  * Running on all addresses (0.0.0.0)
medtronic-hand-tracker |  * Running on http://127.0.0.1:9001
medtronic-hand-tracker |  * Running on http://172.22.0.3:9001
medtronic-hand-tracker | INFO:werkzeug:Press CTRL+C to quit
medtronic-frontend | 
medtronic-frontend | > medtronic-website@0.1.0 start
medtronic-frontend | > react-scripts start
medtronic-frontend | 
medtronic-frontend | (node:26) [DEP_WEBPACK_DEV_SERVER_ON_AFTER_SETUP_MIDDLEWARE] DeprecationWarning: 'onAfterSetupMiddleware' option is deprecated. Please use the 'setupMiddlewares' option.
medtronic-frontend | (Use `node --trace-deprecation ...` to show where the warning was created)
medtronic-frontend | (node:26) [DEP_WEBPACK_DEV_SERVER_ON_BEFORE_SETUP_MIDDLEWARE] DeprecationWarning: 'onBeforeSetupMiddleware' option is deprecated. Please use the 'setupMiddlewares' option.
medtronic-frontend | Starting the development server...
medtronic-frontend | 
medtronic-frontend | Compiled successfully!
medtronic-frontend | 
medtronic-frontend | You can now view medtronic-website in the browser.
medtronic-frontend | 
medtronic-frontend |   Local:            http://localhost:3000
medtronic-frontend |   On Your Network:  http://172.22.0.4:3000
medtronic-frontend | 
medtronic-frontend | Note that the development build is not optimized.
medtronic-frontend | To create a production build, use npm run build.
medtronic-frontend | 
medtronic-frontend | webpack compiled successfully
medtronic-hand-tracker | INFO:werkzeug:172.22.0.1 - - [05/Mar/2025 07:48:47] "GET /api/hand-tracking-stream HTTP/1.1" 200 -
medtronic-hand-tracker | INFO:werkzeug:172.22.0.1 - - [05/Mar/2025 07:48:47] "GET /api/hand-tracking HTTP/1.1" 404 -
medtronic-hand-tracker | INFO:werkzeug:172.22.0.1 - - [05/Mar/2025 07:48:47] "GET /api/hand-tracking HTTP/1.1" 404 -



