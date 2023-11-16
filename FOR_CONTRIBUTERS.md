# For Contributers

For contributing to this repo you need to have following installed on your machine.

1. git
2. Node 16+

## How to start working

1. Take a clone of this repo using the command:
```bash
git clone git@github.com:Shoaib8433/DevSecOpsRnD.git
```
2. Follow the branching structure as mentioned [here](./FOR_CONTRIBUTERS.md#branching-policy).

3. Install the necessary dependencies
```bash
npm install
```

4. Make changes to the repo.
5. To make a commit, this repo is secured to use only conventional commits format, you need to run:
```bash
npm run cz
```

## Branching Policy

Branching will be as follows:

```bash
                       (TAG 0.1.0)
0---------------------0---------------- main
 \                   /
  \                 (TAG 0.1.0-alpha)
   0---------------0------  development
    \             /
     0---0---0---0----- (feature|fix)
```

## Guidelines

- Pushing code to 'main' is strictly prohibited.
- Moving to higher environment needs PR Merge with approvals.