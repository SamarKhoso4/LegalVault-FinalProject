# LegalVault Operational Runbook

## Purpose

This runbook explains how a small law office would operate and support the LegalVault document portal. It covers document uploads, security checks, Python inventory generation, access testing, troubleshooting, and cleanup.

## Uploading Legal Documents to AWS S3

1. Sign in to the AWS Management Console.
2. Open Amazon S3.
3. Select the LegalVault S3 bucket.
4. Open the correct folder:
   - Intake
   - Casenotes
   - Clientletters
   - Policies
5. Upload the appropriate document.
6. Confirm the file appears in the correct folder.

## Checking Security Settings

1. Open the LegalVault S3 bucket.
2. Go to the Permissions tab.
3. Confirm that Block Public Access is enabled.
4. Go to the Properties tab.
5. Confirm that server-side encryption is enabled.
6. Confirm that bucket versioning is enabled if it was configured.

## Running the Python Inventory Script

1. Open Terminal.
2. Navigate to the project folder.
3. Run:

```bash
python3 legalvault_inventory.py