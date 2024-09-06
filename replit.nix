{pkgs}: {
  deps = [
    pkgs.mailutils
    pkgs.python312Packages.uvicorn
    pkgs.postgresql
    pkgs.python312Packages.alembic
  ];
}
