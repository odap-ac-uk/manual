From Andy Law Sept 2022:

The current system was set up as part of the original negotiation with NHS Digital, or NHSX or whatever they were called at that time. Gary Leeming would have been the key player in setting that up. The effective “customer support rep” in NHS Digital has been Helen Buckels (helen.buckels@nhs.net). More recently Francesca Glancy (francesca.glancy1@nhs.net) has been pro-active.

The process operates through what is known as the NHS Digital Secure Electronic File Transfer system (SEFT). There are credentials allocated that allow the user to upload data, and separate credentials to allow a user to download the matched returned data.

Whoever takes over the process of up and downloading will need their own credentials setting up.

The current project ID seems to be "NIC-402963-P0Y5D”, which forms the first part of my username within the system.

The data need to be presented in a particular file format. It’s comma-separated and contains 24 columns, the vast majority of which are empty. The file MUST have a specific set of column headers on the first row and it MUST BE PRESENTED IN WINDOWS CRLF FORMAT, otherwise the system breaks.

The file MUST be named "NIC-402963-P0Y5D.csv”, otherwise the system breaks.

At the NHS Digital end is some kind of database. The last column in each line of the submitted file contains the word “ADD” or “DELETE” which results in the record on that line being added or deleted from the collected set. HOWEVER, you may not combine ADD and DELETE within the same file, otherwise the system breaks.

You may submit no more than ONE FILE PER DAY, otherwise the system breaks.

If your file contains anything that causes the receiving system distress in any way, you’ll find out when it emails you the morning after submission with an unhelpful error message.

Successful submission is signalled by a complete lack of return communication.

Unfortunately, total system failure is also signalled by a complete lack of return communication.

It is not possible to retrieve a list of IDs currently submitted and held in the accumulated pool at the NHS end. In order to submit a new cohort, it’s first necessary to submit a list of currently-submitted IDs with a DELETE command (last column of each row), wait a day for no response and then submit a new set of IDs with “ADD” in the last column of each row. Then wait another day. Despite submitting the exact same data file with the word “ADD” crossed out and replaced with “DELETE”, the remote system will still manage to accumulate records which are impossible to delete unless one asks an NHSD grown-up nicely.


Eventually NHSD will match your data and email to say “There is new data”. Matched data are retrieved from the SEFT Download system which is web-based and defies all efforts to automate. Someone then has to download each of up to 160 individual files (clear text, unencrypted) by clicking on them individually. I have been doing this on a “secure” separate system, then encrypting the downloaded data using 7z. The downloaded matched data are then uploaded to Andrew Brooks/Lucy Norris for onward processing. That was initially via a web-drop interface but latterly has been via SFTP. This receiving system requires the uploaded file to be named “isaric-*” to trigger some automatic routing behind the scenes. I usually send the archive passphrase to Andrew and Lucy by email.

I’m glad that some part of the pain that I had to go through in order to get this to work was seemingly worthwhile in the overall project, but no part of me will be sad to hand this task on to someone else. 