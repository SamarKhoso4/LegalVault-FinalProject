# LegalVault Access-Control Matrix

## Purpose

This access-control matrix defines which staff roles should have access to each category of legal document in the LegalVault system. The goal is to follow the principle of least privilege, meaning users should only receive access to the files they need for their role.

| Role | Intake Forms | Case Notes | Client Letters | Office Policies |
|---|---|---|---|---|
| Attorney | View/Edit | View/Edit | View/Edit | View |
| Paralegal | View/Edit | View | View/Edit | View |
| Receptionist | View/Edit | No Access | No Access | View |
| Public User | No Access | No Access | No Access | No Access |

## Least-Privilege Explanation

Attorneys have the broadest access because they are responsible for reviewing legal matters and client communications. Paralegals have access to most working documents but should have more limited access than attorneys. Receptionists only need access to intake forms and general office policies. Public users should not have direct access to any private legal documents.

## Security Rationale

This model reduces the risk of unauthorized access to sensitive legal information. Case notes and client letters are treated as confidential because they may contain legal strategy, client facts, or internal work product. Public access should remain blocked unless a document is intentionally shared through a controlled method such as a temporary presigned URL.