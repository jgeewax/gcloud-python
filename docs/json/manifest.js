{
  // this will be used to generate links for things like repo issues, etc.
  //   => 'https://github.com/GoogleWebPlatform/gcloud-' + manifest.lang + '/issues'
  "lang": "python",

  // on certain pages we'll be displaying the friendly version of the language
  "friendlyLang": "Python",

  // for code examples we're using highlightjs (https://github.com/isagalaev/highlight.js)
  // use this key to specify the highlight flavor you want
  "markdown": "python",

  // this will be an array of all the available releases
  "versions": [
    "v0.7.1",
    "v0.7.0",
    "v0.6.0",
    "v0.5.0",
    "master"
  ],

  // directory containing content e.g - versions/{{version}}/{{service.contents}}
  //  => versions/master/bigquery/index.json
  "content": "versions",

  // since the landing pages content can't really be generated, we decided to go with HTML
  // this will simply be dropped into the page via ng-include
  // https://github.com/callmehiphop/gcloud-common/blob/shared-docs/site/src/app/home/home.html#L7
  "home": "home.html",

  // this is an optional HTML file that will be injected into the beginning of each API page as an
  // expandable section. See the "Getting started with gcloud" section at the top of an API page
  // http://googlecloudplatform.github.io/gcloud-node/#/docs/v0.27.0/bigquery
  "overview": "getting-started.html",

  // This will act as a table of contents of sorts for the "Getting Started" sections
  // this will follow the JSON hierarchy described at https://github.com/GoogleCloudPlatform/gcloud-node/issues/1084#issuecomment-174528636
  // if a relative link is found for content, the app will assume that it is versioned
  //   => {{content directory}}/{{current version}}/{{markdown file}}
  //
  // You can use the "implemented" key to show/display a certain guide for specific versions
  // There's also an optional "edit" key to provide a URL to edit the markdown file
  "guides": [{
    "title": "Authentication",
    "id": "authentication",
    "edit": "https://github.com/GoogleCloudPlatform/gcloud-common/edit/master/authentication/readme.md",
    "contents": [
      "https://raw.githubusercontent.com/GoogleCloudPlatform/gcloud-common/master/authentication/readme.md",
      "authentication.md"
    ]
  }, {
    "title": "FAQ",
    "id": "faq",
    "edit": "https://github.com/GoogleCloudPlatform/gcloud-common/edit/master/faq/readme.md",
    "contents": [
      "https://raw.githubusercontent.com/GoogleCloudPlatform/gcloud-common/master/faq/readme.md",
      "faq.md"
    ]
  }, {
    "title": "Troubleshooting",
    "id": "troubleshooting",
    "edit": "https://github.com/GoogleCloudPlatform/gcloud-common/edit/master/troubleshooting/readme.md",
    "contents": [
      "https://raw.githubusercontent.com/GoogleCloudPlatform/gcloud-common/master/troubleshooting/readme.md",
      "troubleshooting.md"
    ]
  }, {
    "title": "Contributing",
    "id": "contributing",
    "edit": "https://github.com/GoogleCloudPlatform/gcloud-common/edit/master/contributing/readme.md",
    "contents": "https://raw.githubusercontent.com/GoogleCloudPlatform/gcloud-common/master/contributing/readme.md"
  }],

  // This will follow the JSON hierarchy described at https://github.com/GoogleCloudPlatform/gcloud-node/issues/1084#issuecomment-174528636
  // This will describe the navigation for the API section of the docs, the required fields are
  // "title" and "contents". You can optionally define "implemented" to specify when a service or page within
  // the service was introduced
  "services": [{
    "id": "gcloud",
    "contents": "index.json"
  }, {
    "title": "BigQuery",
    "id": "bigquery",
    "implemented": ">=0.10.0",
    "contents": "bigquery/index.json",
    "nav": [{
      "title": "Dataset",
      "id": "dataset",
      "contents": "bigquery/dataset.json"
    }, {
      "title": "Job",
      "id": "job",
      "contents": "bigquery/job.json"
    }, {
      "title": "Table",
      "id": "table",
      "contents": "bigquery/table.json"
    }]
  }, {
    "title": "Compute",
    "id": "compute",
    "implemented": ">=0.20.0",
    "contents": "compute/index.json",
    "nav": [{
      "title": "Address",
      "id": "address",
      "contents": "compute/address.json"
    }, {
      "title": "Disk",
      "id": "disk",
      "contents": "compute/disk.json"
    }, {
      "title": "Firewall",
      "id": "firewall",
      "contents": "compute/firewall.json"
    }, {
      "title": "Network",
      "id": "network",
      "contents": "compute/network.json"
    }, {
      "title": "Operation",
      "id": "operation",
      "contents": "compute/operation.json"
    }, {
      "title": "Region",
      "id": "region",
      "contents": "compute/region.json"
    }, {
      "title": "Snapshot",
      "id": "snapshot",
      "contents": "compute/snapshot.json"
    }, {
      "title": "VM",
      "id": "vm",
      "contents": "compute/vm.json"
    }, {
      "title": "Zone",
      "id": "zone",
      "contents": "compute/zone.json"
    }]
  }, {
    "title": "DNS",
    "id": "dns",
    "implemented": ">=0.18.0",
    "contents": "dns/index.json",
    "nav": [{
      "title": "Zone",
      "id": "zone",
      "contents": "dns/zone.json"
    }, {
      "title": "Record",
      "id": "record",
      "contents": "dns/record.json"
    }, {
      "title": "Change",
      "id": "change",
      "contents": "dns/change.json"
    }]
  }, {
    "title": "Datastore",
    "id": "datastore",
    "contents": "datastore/index.json",
    "nav": [{
      "title": "Dataset",
      "id": "dataset",
      "contents": "datastore/dataset.json"
    }, {
      "title": "Transaction",
      "id": "transaction",
      "implemented": ">=0.8.0",
      "contents": "datastore/transaction.json"
    }, {
      "title": "Query",
      "id": "query",
      "contents": "datastore/query.json"
    }]
  }, {
    "title": "Logging",
    "id": "logging",
    "implemented": ">=0.27.0",
    "contents": "logging/index.json",
    "nav": [{
      "title": "Entry",
      "id": "entry",
      "contents": "logging/entry.json"
    }, {
      "title": "Log",
      "id": "log",
      "contents": "logging/log.json"
    }, {
      "title": "Sink",
      "id": "sink",
      "contents": "logging/sink.json"
    }]
  }, {
    "title": "Prediction",
    "id": "prediction",
    "implemented": ">=0.27.0",
    "contents": "prediction/index.json",
    "nav": [{
      "title": "Model",
      "id": "model",
      "contents": "prediction/model.json"
    }]
  }, {
    "title": "PubSub",
    "id": "pubsub",
    "implemented": ">=0.8.0",
    "contents": "pubsub/index.json",
    "nav": [{
      "title": "Topic",
      "id": "topic",
      "contents": "pubsub/topic.json"
    }, {
      "title": "Subscription",
      "id": "subscription",
      "contents": "pubsub/subscription.json"
    }]
  }, {
    "title": "Resource",
    "id": "resource",
    "implemented": ">=0.22.0",
    "contents": "resource/index.json",
    "nav": [{
      "title": "Project",
      "id": "project",
      "contents": "resource/project.json"
    }]
  }, {
    "title": "Search",
    "id": "search",
    "implemented": ">=0.16.0",
    "contents": "search/index.json",
    "nav": [{
      "title": "Index",
      "id": "index",
      "contents": "search/index-class.json"
    }, {
      "title": "Document",
      "id": "document",
      "contents": "search/document.json"
    }, {
      "title": "Field",
      "id": "field",
      "contents": "search/field.json"
    }]
  }, {
    "title": "Storage",
    "id": "storage",
    "contents": "storage/index.json",
    "nav": [{
      "title": "Bucket",
      "id": "bucket",
      "implemented": ">=0.1.0",
      "contents": "storage/bucket.json"
    }, {
      "title": "Channel",
      "id": "channel",
      "implemented": ">=0.26.0",
      "contents": "storage/channel.json"
    }, {
      "title": "File",
      "id": "file",
      "implemented": ">=0.9.0",
      "contents": "storage/file.json"
    }]
  }],

  "package": {
    "title": "npm",
    "href": "https://www.npmjs.com/package/gcloud"
  }
}
