+---------------------+     +---------------------+
|     Frontend        |<--->|     Backend         |
|  (Web Application)  |     |  (API Server)       |
|  (Admin Dashboard)  |     |  (Middleware)       |
+---------------------+     |  (Views/Controllers)|
                            |  (Task Queue)       |
                            +---------------------+
                                    |
                                    |
                                    v
                            +---------------------+
                            |    Database (MySQL) |
                            +---------------------+
                                    |
                                    |
                                    v
                            +---------------------+
                            | External Services   |
                            | (Elasticsearch,     |
                            |  Stripe, Email)     |
                            +---------------------+
                                    |
                                    |
                                    v
                            +---------------------+
                            |     Utilities       |
                            | (Cache, File Storage|
                            |  Logging & Monitoring)|
                            +---------------------+
