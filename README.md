# Investigating Suspicious TCP Behavior

I started this investigation by following installing the silk fedora vm from https://tools.netsa.cert.org/livedvd.html#. I then downloaded the data set from https://tools.netsa.cert.org/silk/referencedata.html and followed the instructions for unpacking and using rwfilter. Lastly I downloaded the silk data analysis book from https://tools.netsa.cert.org/silk/analysis-handbook.pdf and began on chapter 7. 

## Level 0: Which TCP Requests are Suspicious. 

The purpose of this case study is to identify incoming and outgoing tcp requests and attempt to find  a pattern that will help guide towards recognizing what is suspicious behavior. Follwing the steps below using the commands provided in the book we can take a look at the incoming and outgoing tcp requests, the ports they are on, and the number of requests. I have added a folder to this repo with the commands I used to accomplish and visualize the data. 
### Steps: 
   1. Use rwfilter to read all incoming TCP traffic for sensors S0 through S4   
  ```bash
   ./inbound_tcp_count_sort > inbound.csv && ./tcp_port_graph.py inbound.csv
   ```
   This gives us a graph showing the port with the number of records:
   ![](images/inboundTCP.png)

   2. Use rwfilter to read all outgoing TCP traffic for sensors S0 through S4
   ```bash
   ./outbound_tcp_count_sort > outbound.csv && ./tcp_port_graph.py outbound.csv
   ```
   This gives us a graph showing the outbound tcp requests by port and number of records. 
   ![](images/outboundGraph.png)

   3. Now we can compare the two using our third graph:
   ```bash
   ./outbound_vs_inbound_graph.py
   ```

   This gives us our inbound and outbound side by side:
   ![](images/inboundVoutbound.png)
   