# Master files

The `.md` files in this directory are the master versions. Any changes should be committed using git.


# Process for including edits from word versions

Some users will make changes to the word versions of these files. These changes can be incorporated into the master `.md` files using the following process:

1. Convert to markdown
```
pandoc --wrap=none ../_documents/Governance/DataAccess/DAGC_ToR.docx -o temp_DACG_ToR.md
pandoc --wrap=none ../_documents/Governance/DataAccess/DataAccessReviewProcess.docx -o temp_DataAcccessReviewProcess.md
pandoc --wrap=none ../_documents/Governance/DataAccess/PRP_TOR.docx -o temp_PRP_ToR.md
pandoc --wrap=none ../_documents/Governance/PartnershipSteeringGp/PSG_ToR.docx -o temp_PSG_ToR.md

```

2. Compare documents using the document comparison software of your choice. (e.g. sublimerge, git)

3. Copy any accepted changes into the master markdown document

4. Follow the command in the relevant document to generate a new, clean word version

5. Delete temporary files

6. Commit to git and upload to github




