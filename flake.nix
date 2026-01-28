{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in
    {
      devShells.${system}.default = pkgs.mkShell {

        buildInputs = with pkgs; [
          (pkgs.python3.withPackages (
            python-pkgs: with python-pkgs; [
              # select Python packages here
              pandas
              requests
		click
            ]
          ))
          fpc
          lazarus
        ];

      };
    };
}
