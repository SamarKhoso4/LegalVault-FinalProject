# Secure Cloud-Based Legal Document Portal

## Project Overview

LegalVault is a secure cloud-based document portal prototype for a small law office. The project demonstrates how sample legal documents can be organized, protected, inventoried, and tested using AWS S3 and Python automation.

## Organization Scenario

The organization is a small law office that needs a secure and low-cost way to store and manage sample legal documents such as intake forms, case notes, client letters, and office policies.

## Technical Components

### AWS S3 Build

The AWS portion of the project included:
- A private S3 bucket for legal documents
- Folder organization for legal file categories
- Block Public Access enabled
- Server-side encryption enabled
- Versioning enabled
- Authorized access testing
- Public access denied testing
- Presigned URL testing

### Python Automation Script

The Python script scans the local Sampledocuments folder and creates a CSV inventory. The inventory includes:
- File name
- Folder name
- Document type
- Sensitivity level
- Suggested access roles

## Testing Summary

Success tests:
- Authorized AWS access worked.
- The Python script successfully generated a document inventory CSV.
- A presigned URL temporarily opened a private file.

Failure tests:
- A public S3 object URL returned Access Denied.
- The Python script showed an error when the Sampledocuments folder was renamed.

## Security Note

All legal documents used in this project are fake sample files. No real client information or confidential legal data is included.