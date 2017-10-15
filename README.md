http://www.dropwizard.io/1.2.0/docs/getting-started.html

Dropwizard projects have a main method that starts everything.

1. Jetty for HTTP
2. Jersey for REST
3. Jackson for JSON
4. Metrics for metrics

5. Guava for utils
6. Logback and slf4j for logging
7. Hibernate validator for bean validation
8. Apache HttpClient and Jersey for HTTP calls
9. JDBI for RDMBS
10. Liquibase for data migrations
11. Freemarker/Mustache for templating
12. Joda time for date and time

## Getting started

```
mvn archetype:generate \
	-DarchetypeGroupId=io.dropwizard.archetypes \
	-DarchetypeArtifactId=java-simple \
	-DarchetypeVersion=[REPALCE WITH A VALID DROPWIZARD VERSION]
```

