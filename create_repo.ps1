# ---------------------------
# CONFIG - EDIT THESE
# ---------------------------
$RepoName = "youtube-data-scraper"          # GitHub repo name
$Description = "Scrape Youtube Data Easily"  # Repo description
$Private = $false                             # $true = private, $false = public

# ---------------------------
# CHECK FOR .git
# ---------------------------
if (!(Test-Path ".git")) {
    Write-Host "Initializing local Git repository..."
    git init
}

# ---------------------------
# STAGE FILES
# ---------------------------
Write-Host "Adding files to Git..."
git add .

# ---------------------------
# COMMIT FILES
# ---------------------------
Write-Host "Committing files..."
git commit -m "Initial commit"

# ---------------------------
# CREATE GITHUB REPO
# ---------------------------
if ($Private) {
    Write-Host "Creating PRIVATE GitHub repository..."
    gh repo create $RepoName --private --description $Description --source=. --remote=origin --push
} else {
    Write-Host "Creating PUBLIC GitHub repository..."
    gh repo create $RepoName --public --description $Description --source=. --remote=origin --push
}

Write-Host "✅ Repository '$RepoName' created and pushed!"