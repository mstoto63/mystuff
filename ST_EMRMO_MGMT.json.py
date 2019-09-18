{
  "data": {
    "tailf-ncs:devices": {
      "template": [
        {
          "name": "ST_EMRMO_MGMT",
          "config": {
            "snmp:snmp": {
              "agent": {
                "enabled": "true",
                "ip": "127.0.0.1",
                "udp-port": "161",
                "version": {
                  "v3": [null]
                },
                "engine-id": {
                  "enterprise-number": "42359",
                  "from-ip": "{$v_GL-RMO-Control-VR_4_Router_ID__vrRouteId}"
                }
              },
              "usm": {
                "local": {
                  "user": [
                    {
                      "name": "geminiV3128",
                      "auth": {
                        "sha": {
                          "password": "L3tm3inV3Aut"
                        }
                      },
                      "priv": {
                        "aes": {
                          "password": "L3tm3inV3Enc"
                        }
                      }
                    }
                  ]
                }
              },
              "target-source": "{$v_GL-RMO-Control-VR_4_Local_address__vrRouterAddress}",
              "target": [
                {
                  "name": "DEFRA1-SNMP-Trap",
                  "ip": "167.16.53.45",
                  "udp-port": "162",
                  "timeout": "15",
                  "retries": "3",
                  "usm": {
                    "user-name": "geminiV3128",
                    "sec-level": "auth-priv"
                  }
                },
                {
                  "name": "DEFRA2-SNMP-Trap",
                  "ip": "167.16.59.44",
                  "udp-port": "162",
                  "timeout": "15",
                  "retries": "3",
                  "usm": {
                    "user-name": "geminiV3128",
                    "sec-level": "auth-priv"
                  }
                }
              ],
              "vacm": {
                "group": [
                  {
                    "name": "FD",
                    "member": [
                      {
                        "sec-name": "geminiV3128",
                        "sec-model": ["usm"]
                      }
                    ],
                    "access": [
                      {
                        "sec-model": "usm",
                        "sec-level": "auth-priv",
                        "read-view": "geminiv3128",
                        "notify-view": "geminiv3128"
                      }
                    ]
                  }
                ],
                "view": [
                  {
                    "name": "geminiv3128",
                    "subtree": [
                      {
                        "oids": "1.2",
                        "included": [null]
                      },
                      {
                        "oids": "1.3",
                        "included": [null]
                      },
                      {
                        "oids": "1.3.6.1",
                        "included": [null]
                      }
                    ]
                  }
                ]
              }
            },
            "cos:class-of-services": {
            },
            "clear:clear": {
              "statistics": {
                "adc:adc": {
                  "policies": {
                  }
                },
                "cgnat:cgnat": {
                },
                "cos:class-of-service": {
                },
                "crypto:crypto": {
                  "pki": {
                  }
                },
                "eoam:eoam": {
                },
                "sdwan:sd-wan": {
                },
                "security:ssl": {
                },
                "security:security": {
                  "captive-portal": {
                  }
                },
                "security:object": {
                  "snat": {
                  }
                },
                "user-identification:user-identification": {
                },
                "vfp:vfp": {
                }
              },
              "dhcp:dhcp": {
                "statistics": {
                }
              },
              "interfaces:interfaces": {
              }
            },
            "crypto:crypto": {
              "pki": {
              }
            },
            "diagnostics:diagnostics": {
            },
            "eoam:eoam": {
              "connectivity-fault-management": {
              }
            },
            "interfaces:lacp": {
            },
            "interfaces:pppoe": {
            },
            "interfaces:interfaces": {
              "port": {
              },
              "wwan": {
              },
              "tvi": [
                {
                  "name": "tvi-0/2601",
                  "enable": "true",
                  "mode": "ipsec",
                  "type": "paired",
                  "mtu": "1400",
                  "paired-interface": "tvi-0/2600",
                  "unit": [
                    {
                      "name": "0",
                      "enable": "true",
                      "family": {
                        "inet": {
                          "address": [
                            {
                              "addr": "169.254.7.209/31"
                            }
                          ]
                        }
                      }
                    }
                  ]
                },
                {
                  "name": "tvi-0/2600",
                  "enable": "true",
                  "mode": "ipsec",
                  "type": "paired",
                  "mtu": "1400",
                  "paired-interface": "tvi-0/2601",
                  "unit": [
                    {
                      "name": "0",
                      "enable": "true",
                      "family": {
                        "inet": {
                          "address": [
                            {
                              "addr": "169.254.7.208/31"
                            }
                          ]
                        }
                      }
                    }
                  ]
                }
              ]
            },
            "ipv6-neighbor:ipv6": {
            },
            "logger:debug": {
            },
            "ntp:ntp": {
              "server": [
                {
                  "name": "10.181.252.8",
                  "source-interface": "tvi-0/9.0",
                  "routing-instance": "GL-RMO-Control-VR",
                  "enable": "true",
                  "version": "4"
                },
                {
                  "name": "10.181.252.4",
                  "source-interface": "tvi-0/9.0",
                  "routing-instance": "GL-RMO-Control-VR",
                  "enable": "true",
                  "version": "4"
                },
                {
                  "name": "10.174.252.4",
                  "source-interface": "tvi-0/9.0",
                  "routing-instance": "GL-RMO-Control-VR",
                  "enable": "true",
                  "version": "4"
                }
              ]
            },
            "oam:alarms": {
              "alarm": [
                {
                  "name": "all",
                  "destinations": ["syslog", "snmp"]
                }
              ]
            },
            "org:orgs": {
              "org": [
                {
                  "name": "GL-RMO",
                  "appliance-owner": [null],
                  "available-routing-instances": ["GL-RMO-Control-VR"],
                  "owned-routing-instances": ["GL-RMO-Control-VR"],
                  "options": {
                    "session-limit": "1000000"
                  },
                  "traffic-identification": {
                    "using": ["tvi-0/2601.0", "tvi-0/2600.0"]
                  },
                  "sessions": {
                  },
                  "policy": {
                    "quota": {
                    }
                  },
                  "sdwan:sd-wan": {
                    "sla-monitor": {
                    },
                    "statistics": {
                    }
                  },
                  "security:security": {
                  }
                }
              ],
              "org-services": [
                {
                  "name": "GL-RMO",
                  "options": {
                  },
                  "access:access": {
                    "ldap": {
                    },
                    "radius": {
                    }
                  },
                  "adc:adc": {
                    "monitors": {
                    },
                    "profiles": {
                      "service-profiles": {
                      },
                      "persistence-profiles": {
                      }
                    },
                    "policies": {
                    },
                    "policy-group": {
                    },
                    "lb": {
                    },
                    "glb": {
                      "dnssec": {
                        "sign-keys": {
                        }
                      }
                    }
                  },
                  "alg:alg": {
                  },
                  "appid:application-identification": {
                    "statistics": {
                      "application": {
                      }
                    }
                  },
                  "cgnat:cgnat": {
                    "map-t": {
                    },
                    "pools": {
                      "pool": [
                        {
                          "name": "Pool-Overlay-ESP",
                          "address": ["{$v_tvi-0-9_-_Unit_0_Static_address__tunnelStaticAddress}"],
                          "routing-instance": "GL-RMO-Control-VR",
                          "source-port": {
                            "allocation-scheme": "automatic",
                            "random-allocation": [null]
                          }
                        }
                      ]
                    },
                    "rules": {
                      "rule": [
                        {
                          "name": "HostRule-Overlay",
                          "precedence": "1",
                          "paired-site": "false",
                          "from": {
                            "source-zone": ["HOST-Overlay-Zone"]
                          },
                          "then": {
                            "translated": {
                              "translation-type": "napt-44",
                              "source-pool": "Pool-Overlay-ESP",
                              "filtering-type": "none",
                              "mapping-type": "none"
                            }
                          }
                        }
                      ]
                    },
                    "softwire-concentrators": {
                    }
                  },
                  "cos:class-of-service": {
                    "rw-rules": {
                    },
                    "qos-policies": {
                      "qos-policy-group": [
                        {
                          "name": "Default-Policy"
                        }
                      ]
                    },
                    "app-qos-policies": {
                      "app-qos-policy-group": [
                        {
                          "name": "Default-Policy"
                        }
                      ]
                    }
                  },
                  "crypto:crypto": {
                    "pki": {
                    }
                  },
                  "dhcp:dhcp": {
                    "dhcp4-server-and-relay": {
                    },
                    "dhcp6-server-and-relay": {
                    },
                    "statistics": {
                    }
                  },
                  "ipsec:ipsec": {
                  },
                  "lef:lef": {
                    "collectors": {
                      "collector": [
                        {
                          "name": "LEF-Collector-log_collector1",
                          "destination-address": "10.130.48.3",
                          "destination-port": "1234",
                          "source-address": "{$v_GL-RMO-Control-VR_4_Local_address__vrRouterAddress}",
                          "routing-instance": "GL-RMO-Control-VR",
                          "transmit-rate": "10000",
                          "pending-queue-limit": "2048",
                          "template-resend-interval": "60",
                          "transport": "tcp",
                          "template": "Default-LEF-Template"
                        },
                        {
                          "name": "LEF-Collector-log_collector2",
                          "destination-address": "10.130.48.4",
                          "destination-port": "1234",
                          "source-address": "{$v_GL-RMO-Control-VR_4_Local_address__vrRouterAddress}",
                          "routing-instance": "GL-RMO-Control-VR",
                          "transmit-rate": "10000",
                          "pending-queue-limit": "2048",
                          "template-resend-interval": "60",
                          "transport": "tcp",
                          "template": "Default-LEF-Template"
                        },
                        {
                          "name": "LEF-Collector-log_collector3",
                          "destination-address": "10.130.48.5",
                          "destination-port": "1234",
                          "source-address": "{$v_GL-RMO-Control-VR_4_Local_address__vrRouterAddress}",
                          "routing-instance": "GL-RMO-Control-VR",
                          "transmit-rate": "10000",
                          "pending-queue-limit": "2048",
                          "template-resend-interval": "60",
                          "transport": "tcp",
                          "template": "Default-LEF-Template"
                        }
                      ]
                    },
                    "collector-groups": {
                      "collector-group": [
                        {
                          "collector-group-name": "Default-Collector-Group",
                          "collectors": ["LEF-Collector-log_collector1", "LEF-Collector-log_collector3", "LEF-Collector-log_collector2"]
                        }
                      ]
                    },
                    "templates": {
                      "template": [
                        {
                          "name": "Default-LEF-Template",
                          "type": "ipfix"
                        }
                      ]
                    },
                    "profiles": {
                      "profile": [
                        {
                          "name": "Default-Logging-Profile",
                          "collector-group": "Default-Collector-Group"
                        }
                      ]
                    },
                    "default-profile": "Default-Logging-Profile"
                  },
                  "pbf:pbf": {
                  },
                  "sdwan:sd-wan": {
                    "policies": {
                      "sdwan-policy-group": [
                        {
                          "name": "Default-Policy",
                          "rules": {
                            "statistics": {
                            }
                          }
                        }
                      ]
                    }
                  },
                  "security:security": {
                    "profiles": {
                      "av": {
                      },
                      "dos": {
                      },
                      "url-filtering": {
                      },
                      "ips": {
                        "statistics": {
                        }
                      },
                      "ip-filtering": {
                      },
                      "file-filtering": {
                      }
                    },
                    "uid": {
                    },
                    "captive-portal": {
                    },
                    "ips": {
                    },
                    "access-policies": {
                      "access-policy-group": [
                        {
                          "name": "Default-Policy"
                        }
                      ]
                    },
                    "ip-filtering": {
                    },
                    "ssl": {
                    },
                    "url-filtering": {
                      "statistics": {
                      }
                    },
                    "logs": {
                      "logging-control": {
                      }
                    }
                  },
                  "security:objects": {
                    "zones": {
                      "zone": [
                        {
                          "name": "HOST-Overlay-Zone",
                          "interface-list": ["tvi-0/2600.0"]
                        },
                        {
                          "name": "HOST-Overlay-GRT-Zone",
                          "interface-list": ["tvi-0/2601.0"]
                        }
                      ]
                    },
                    "snat": {
                    }
                  },
                  "security:dns": {
                  },
                  "sfc:service-filters": {
                  },
                  "traffic-mirroring:traffic-mirroring": {
                  },
                  "traffic-monitoring:traffic-monitoring": {
                  },
                  "url-filtering:url-filtering": {
                    "settings": {
                    }
                  },
                  "user-identification:user-identification": {
                    "local-database": {
                    },
                    "external-database": {
                    },
                    "live-users": {
                    }
                  },
                  "vfp:vfp": {
                  }
                }
              ]
            },
            "predefined:predefined": {
            },
            "predefined-appid-groups-filters:predefined-appid-groups-filters": {
            },
            "rfd:resource-management": {
            },
            "routing-module:routing-options": {
              "static": {
                "route": {
                  "static-route-list": [
                    {
                      "ip-prefix": "10.82.8.64/32",
                      "next-hop": "169.254.7.208",
                      "interface": "none",
                      "preference": "1"
                    },
                    {
                      "ip-prefix": "10.83.15.71/32",
                      "next-hop": "169.254.7.208",
                      "interface": "none",
                      "preference": "1"
                    },
                    {
                      "ip-prefix": "10.68.196.61/32",
                      "next-hop": "169.254.7.208",
                      "interface": "none",
                      "preference": "1"
                    },
                    {
                      "ip-prefix": "10.68.196.65/32",
                      "next-hop": "169.254.7.208",
                      "interface": "none",
                      "preference": "1"
                    },
                    {
                      "ip-prefix": "10.77.196.65/32",
                      "next-hop": "169.254.7.208",
                      "interface": "none",
                      "preference": "1"
                    },
                    {
                      "ip-prefix": "10.77.196.61/32",
                      "next-hop": "169.254.7.208",
                      "interface": "none",
                      "preference": "1"
                    }
                  ]
                }
              }
            },
            "routing-module:protocols": {
              "bfd": {
              },
              "eoam:eoam": {
              },
              "interfaces:vrrp": {
              }
            },
            "routing-module:routing-instances": {
              "routing-instance": [
                {
                  "name": "GL-RMO-Control-VR",
                  "instance-type": "virtual-router",
                  "interfaces": ["tvi-0/2600.0"],
                  "routing-options": {
                    "static": {
                    }
                  },
                  "protocols": {
                    "bfd": {
                    }
                  },
                  "policy-options": {
                  }
                }
              ]
            },
            "routing-module:policy-options": {
            },
            "routing-vrf:vrf-config": {
              "proto-ra": {
              }
            },
            "security:security": {
              "osspack": {
              },
              "security-package": {
              },
              "ip-filtering": {
              }
            },
            "system:system": {
              "vnf-manager": {
                "ip-addresses": ["10.164.0.0/15", "10.180.243.10/32", "10.174.243.10/32", "10.82.14.0/24", "10.83.13.0/24", "167.16.59.0/24", "167.16.53.0/24"]
              },
              "session": {
              },
              "parameters": {
                "storage": {
                }
              },
              "syslog": {
                "server": [
                  {
                    "name": "10.68.196.61",
                    "enabled": "true",
                    "selector": [
                      {
                        "name": "100",
                        "negate": "false",
                        "comparison": "same_or_higher",
                        "level": "notice",
                        "facility-list": ["all"]
                      }
                    ]
                  },
                  {
                    "name": "10.68.196.65",
                    "enabled": "true",
                    "selector": [
                      {
                        "name": "100",
                        "negate": "false",
                        "comparison": "same_or_higher",
                        "level": "notice",
                        "facility-list": ["all"]
                      }
                    ]
                  },
                  {
                    "name": "10.77.196.61",
                    "enabled": "true",
                    "selector": [
                      {
                        "name": "100",
                        "negate": "false",
                        "comparison": "same_or_higher",
                        "level": "notice",
                        "facility-list": ["all"]
                      }
                    ]
                  },
                  {
                    "name": "10.77.196.65",
                    "enabled": "true",
                    "selector": [
                      {
                        "name": "100",
                        "negate": "false",
                        "comparison": "same_or_higher",
                        "level": "notice",
                        "facility-list": ["all"]
                      }
                    ]
                  }
                ]
              },
              "services": {
              },
              "dhcp-parameters": {
              },
              "time-zone": "Greenwich",
              "users": [
                {
                  "name": "N3t3ng",
                  "password": "L3tm3in@1",
                  "login": "cli",
                  "role": "admin"
                }
              ],
              "service-options": {
                "buffer-parameters": {
                }
              },
              "upgrade-options": {
              },
              "external-aaa": {
                "auth-order": "remote-then-local",
                "tacacs-plus": {
                  "server": [
                    {
                      "host": "10.83.15.71",
                      "key": "Eicoh9ge"
                    },
                    {
                      "host": "10.82.8.64",
                      "key": "Eicoh9ge"
                    }
                  ],
                  "action": ["authentication"]
                }
              },
              "platform": {
                "fwa-1010": {
                }
              }
            },
            "system:erase": {
            },
            "vnf:guest-vnfs": {
              "virtual-machines": {
              }
            },
            "wlan:wlan": {
              "wlan-2.4GHz": {
              },
              "wlan-5GHz": {
              }
            }
          }
        }
      ]
    }
  }
}
