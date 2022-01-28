# servicex_did_demo

 Demo the ServiceX DID Library

## Usage

This is a demo DID finder for the ServiceX project. It can be run in ServiceX and if given an appropriate dataset name, it will return a fixed set of data files to the system.

It is meant to demo usage of the `ServiceX_DID` library, and be used as a template to build new ServiceX DID finders. You'll need to add a `deployment.yaml` to the ServiceX chart in order to get this to work. Please see other `did_finder deployment.yaml` files and pattern it off this one.

## Testing Demo in ServiceX

To test this in ServiceX perform the following steps:

1. Start a servicex instance with the demo did finder running
1. Launch the `sample.simple_query.ipynb` in a notebook server. If you install all development packages in the `toml` file, you'll have everything you need.
1. Run the sample. On a home internet, the sample takes about 20 seconds to complete.

## Creating a new ServiceX DID Finder

To see how this is created see the following files in this repository:

* `src/demo.did.py` - Contains the code that returns a single file if the proper dataset name is queried.
* `Dockerfile` - Builds the container that can run in the ServiceX environment.
* `requirements.txt` - Contains all the packages required to run the did finder.

## Test locally with KinD

* Install kind locally <https://kind.sigs.k8s.io/>
* Launch the cluster with `make createcluster`
* Build the Service Demo container with `make build`
* Make it available inside the KinD cluster with `make load`
* Install ServiceX via Helm with `make servicex`
* Create the Service Demo deployment with `make demo`
* Edit the servicex configuration with `make edit` and replace `cernopendata` with `demo` in `DID_FINDER_DEFAULT_SCHEME` and `VALID_DID_SCHEMES`
* Delete the servicex and the codegen pods so that they are re-created with the new configuration
* Setup forwarding of port 5000 locally with `make forward &`
* Test with `make test`, you should get a request id back similar to `{'request_id': '5847d172-1681-411f-8913-5a1d57aac558'}`
