# Dropwizard

http://www.dropwizard.io/1.2.0/docs/getting-started.html

The entrypoint of a Dropwizard application is a subclass of 'Application'. The project is started as a standalone Java SE app with this class as entrypoint.


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

## Configuration

Each Dropwizard application has got its own subclass of Configuration, which specifies environment-specific parameters. These parameters are specified in a YAML-file, which is deserialized and validated at startup.

- Deserialized by Jackson.
- Validated by Hibernate Validator.

## Application

The dropwizard main class is a subclass of Application, parameterized by the Configuration class above.

## Representation class

An entity can be represented by a Jackson-annotated JavaBean.


## Dropwizard core

- Jetty
- Jersey
- Jackson
- Metrics
- Guava
- Logback
- Hibernate Validator

### CLI?

If you plan of building a Java cli, split your application in three modules – api, client and application. "api" should contain Representations that are used by both the client and the application.

### If not

com.example.myapplication:

- api: Representations. Request and response bodies.
- cli: Commands
- client: Client code that accesses external HTTP services.
- core: Domain implementation; where objects not used in the API such as POJOs, validations, crypto, etc, reside.
- jdbi: Database access classes
- health: Health Checks
- resources: Resources
- MyApplication: The application class
- MyApplicationConfiguration: configuration class


## Application

The main entrypoint of the application.

- A name, used mostly for the command line UI.
- Bundles: features that can be added to the application
- Commands: basic actions to take. For example the built-in 'server' command.

## Configuration

Group related configuration parameters into independent configuration classes.

For example: If your application need configuration to connect to a message queue, we recomment that you create a new MessageQueueFactory-class:

```java
public class MessageQueueFactory {
    @NotEmpty
    private String host;

    @Min(1)
    @Max(65535)
    private int port = 5672;
    @JsonProperty public String getHost() { }
    @JsonProperty public void setHost(String host) { }
    @JsonProperty public int getPort() { }
    @JsonProperty public void setPort(int port) { }

    public MessageQueueClient build(Environment environment) {
        MessageQueueClient client = new MessageQueueClient(getHost(), getPort());
        environment.lifecycle().manage(new Managed() {
            @Override
            public void start() {
            }

            @Override
            public void stop() {
                client.close();
            }
        });
        return client;
    }
}
```

In this example, our factory will automatically tie our MessageQueueClient connection to the lifecycle of our application's environment.

The main configuration class can then include this as a field:

```java
public class ExampleConfiguration extends Configuration {
    @Valid
    @NotNull
    private MessageQueueFactory messageQueue = new MessageQueueFactory();

    @JsonProperty("messageQueue")
    public MessageQueueFactory getMessageQueueFactory() {
        return messageQueue;
    }

    @JsonProperty("messageQueue")
    public void setMessageQueueFactory(MessageQueueFactory factory) {
        this.messageQueue = factory;
    }
}
```

And the Application class can then use your factory to directly construct a client for the message queue.

```
public void run(ExampleConfiguration configuration,
                Environment environment) {
    MessageQueueClient messageQueue =
    	configuration.getMessageQueueFactory().build(environment);
}
```

And in the yaml, it might look like this:

```
messageQueue:
  host: mq.example.com
  port: 5673
```

### Configuration overries

Configuration path overrides can be specified with java system properties with a `wd.` prefix.

```
java -Ddw.logging.level=DEBUG server my-config.json
java -Ddw.server.applicationConnectors[0].port=9090 server my-config.json
java -Ddw.database.properties.hibernate.hbm2ddl.auto=none server my-config.json
java -Ddw.myapp.myserver.hosts=server1,server2,server3 server my-config.json
```

## SSL

Dropwizard can be a SSL terminator, but your need to supply certificates by using a java keystore.

`keytool`


## Bootstrapping

Before the application can provide the command line interface, parse configuration files or run as a server, it must first go through a bootstrapping phase. This phase corresponds to your Application's `initialize` method.

You can add `bundles`, `commands`, or register Jackson modules to allow you to include custom types as part of your configuration class.

## Environment

A Dropwizard `Environment` consists of all the Resources, servlets, filters, health checks, jersey providers, managed objects, tasks and Jersey properties which your application provides.

Each application subclass implements a run method. This is where you should be creating new resource instsances etc, and add them to the given environment.

```
@Override
public void run(ExampleConfiguration config,
                Environment environment) {
    // encapsulate complicated setup logic in factories
    final Thingy thingy = config.getThingyFactory().build();

    environment.jersey().register(new ThingyResource(thingy));
    environment.healthChecks().register("thingy", new ThingyHealthCheck(thingy));
}
```

## Health Checks

For example database connectivity.

```
environment.healthChecks().register("database", new DatabaseHealthCheck(database));
```

```
$ curl http://dw.example.com:8081/healthcheck
{"deadlocks":{"healthy":true},"database":{"healthy":true}}
```

## Managed Objects

Most applications involve objects that needs to be started and stopped: thread pools, database connections etc.

Dropwizard provides the `Managed` interface for this. You can either have the class in question implement the `#start()` and `#stop()` methods, or write a wrapper class that does so.

Adding a `Managed` instance to your application's `Environment` ties that object's lifecycle to that of the application's HTTP Server. Before the server starts, all `start` methods are called. After the server has stopped, all `stop` methods are called.

### Built-in managed objects

There are some managed objects available out of the box. For example:

- ExecutorService
- ScheduledExecutorService


## Bundles

A dropwizard bundle is a reusable group of functionality, used to define blocks of an application's behaviour. For example:

- AssetBundle, serve static assets


### Configured Bundles

Some bundles require configuration parameters. These bundles implement `ConfiguredBundle` and will require your application's `Configuration` subclass to implement a specific interface.

For example, if MyBundle is a ConfiguredBundle<MyConfiguredBundleConfig>, then the application's configuration file must implement MyBundleConfig.

```
public class MyConfiguredBundle implements ConfiguredBundle<MyConfiguredBundleConfig>{

    @Override
    public void run(MyConfiguredBundleConfig applicationConfig, Environment environment) {
        applicationConfig.getBundleSpecificConfig();
    }

    @Override
    public void initialize(Bootstrap<?> bootstrap) {

    }
}

public interface MyConfiguredBundleConfig{

    String getBundleSpecificConfig();

}
```

## Commands

Commands are CLI subcommands (like 'server').

```
public class MyCommand extends Command {
    public MyCommand() {
        // The name of our command is "hello" and the description printed is
        // "Prints a greeting"
        super("hello", "Prints a greeting");
    }

    @Override
    public void configure(Subparser subparser) {
        // Add a command line option
        subparser.addArgument("-u", "--user")
                .dest("user")
                .type(String.class)
                .required(true)
                .help("The user of the program");
    }

    @Override
    public void run(Bootstrap<?> bootstrap, Namespace namespace) throws Exception {
        System.out.println("Hello " + namespace.getString("user"));
    }
}
```

```
public class MyApplication extends Application<MyConfiguration>{
    @Override
    public void initialize(Bootstrap<DropwizardConfiguration> bootstrap) {
        bootstrap.addCommand(new MyCommand());
    }
}
```

```
java -jar <jarfile> hello dropwizard
```

### Configured Commands

A command that extends `ConfiguredCommand<YourAppsConfiguration>`.

```
@Override
public void configure(Subparser subparser) {
    super.configure(subparser);

    // Add a command line option
    subparser.addArgument("-u", "--user")
            .dest("user")
            .type(String.class)
            .required(true)
            .help("The user of the program");
}
```


## Tasks

A `task` is a runtime action that your application provides access to on the administrative port via HTTP. All dropwizard applications start with `gc` and `log-level`.

The execute method of a `task` can be annotated with `@Timed`, `@Metered` and `@ExceptionMetered`.

```
public class TruncateDatabaseTask extends Task {
    private final Database database;

    public TruncateDatabaseTask(Database database) {
        super("truncate");
        this.database = database;
    }

    @Override
    public void execute(ImmutableMultimap<String, String> parameters, PrintWriter output) throws Exception {
        this.database.truncate();
    }
}
```

```
environment.admin().addTask(new TruncateDatabaseTask(database));
```

```
$ curl -X POST http://dw.example.com:8081/tasks/gc
Running GC...
Done!
```

Another example, which consumes a POST entity.

```
public class EchoTask extends PostBodyTask {
    public EchoTask() {
        super("echo");
    }

    @Override
    public void execute(ImmutableMultimap<String, String> parameters, String postBody, PrintWriter output) throws Exception {
        output.write(postBody);
        output.flush();
    }
}
```

## Logging

slf4j with a `Logback` backend. Routes jul, log4j, commons logging through logback.

```
ERROR
Error events that might still allow the application to continue running.
WARN
Potentially harmful situations.
INFO
Informational messages that highlight the progress of the application at coarse-grained level.
DEBUG
Fine-grained informational events that are most useful to debug an application.
TRACE
Finer-grained informational events than the DEBUG level.
```

### Log format

`LEVEL [ISO 8601] who what`
Stack traces with !, for easy greping.

```
TRACE [2010-04-06 06:42:35,271] com.example.dw.Thing: Contemplating doing a thing.
DEBUG [2010-04-06 06:42:35,274] com.example.dw.Thing: About to do a thing.
INFO  [2010-04-06 06:42:35,274] com.example.dw.Thing: Doing a thing
WARN  [2010-04-06 06:42:35,275] com.example.dw.Thing: Doing a thing
ERROR [2010-04-06 06:42:35,275] com.example.dw.Thing: This may get ugly.
! java.lang.RuntimeException: oh noes!
! at com.example.dw.Thing.run(Thing.java:16)
!
```

### Log Configuration

Configured in the yaml file (or sysprop overrides...)

```
logging:
  appenders:
    - type: console
      threshold: WARN
      target: stderr
```

```
logging:
  appenders:
    - type: file
      currentLogFilename: ./logs/example.log
      archivedLogFilenamePattern: ./logs/example-%d.log.gz
      archivedFileCount: 5
      timeZone: UTC
```

Or the log configuration task:

```
curl -X POST -d "logger=com.example.helloworld&level=INFO" http://localhost:8081/tasks/log-level
```

## Application testing

```
public class MyApplicationTest {
    private final Environment environment = mock(Environment.class);
    private final JerseyEnvironment jersey = mock(JerseyEnvironment.class);
    private final MyApplication application = new MyApplication();
    private final MyConfiguration config = new MyConfiguration();

    @Before
    public void setup() throws Exception {
        config.setMyParam("yay");
        when(environment.jersey()).thenReturn(jersey);
    }

    @Test
    public void buildsAThingResource() throws Exception {
        application.run(config, environment);

        verify(jersey).register(isA(ThingResource.class));
    }
}
```

## Banners

`src/main/resources/banner.txt`

```
INFO  [2011-12-09 21:56:37,209] io.dropwizard.cli.ServerCommand: Starting hello-world
                                                 dP
                                                 88
  .d8888b. dP.  .dP .d8888b. 88d8b.d8b. 88d888b. 88 .d8888b.
  88ooood8  `8bd8'  88'  `88 88'`88'`88 88'  `88 88 88ooood8
  88.  ...  .d88b.  88.  .88 88  88  88 88.  .88 88 88.  ...
  `88888P' dP'  `dP `88888P8 dP  dP  dP 88Y888P' dP `88888P'
                                        88
                                        dP

INFO  [2011-12-09 21:56:37,214] org.eclipse.jetty.server.Server: jetty-7.6.0
...
```

## Resources

It's Jersey...


### Metrics

Every resource method can be annotated with `@Timed`, `@Metered` and `@ExceptionMetered`.


### Responses

Return annotated domain objects where possible...

### Error responses

Throw exceptions!

```
    if (!collectionMap.containsKey(collection)) {
        final String msg = String.format("Collection %s does not exist", collection);
        throw new WebApplicationException(msg, Status.NOT_FOUND)
    }
```

Or use exceptionmappers, if needed...

```
env.jersey().register(new IllegalArgumentExceptionMapper(env.metrics()));
```

## Json (de-)serialization

Immutable

```
public class Notification {
    private final String text;

    @JsonCreator
    public Notification(@JsonProperty("text") String text) {
        this.text = text;
    }

    @JsonProperty("text")
    public String getText() {
        return text;
    }
}
```

Advanced mapping

```
@JsonSerialize(using=FunkySerializer.class)
@JsonDeserialize(using=FunkyDeserializer.class)
public class Funky {
    // ...
}
```

`@JsonSnakeCase`


## Streaming output

Jersey's `StreamingOutput` for chunk-encoding.


## HTML Representations

See dropwizard `views`.


## How is it glued together?

When the application starts up, it will spin up a Jetty HTTP server (see `DefaultServerFactory`).

This server will have two handlers:

- application port
- admin port (AdminServlet)

The application port has got an HttpServlet as well. this is composed of `DropwizardResourceConfig`, which is an extension of Jersey's resource configuration that performs scanning to find root resources and provider classes. Ultimately when you call `env.jersey().register(new SomeResouce))`, you are adding to the DropwizardResourceConfig. This config is a jersey Application, so all of your application resources are served from one servlet.

DropwizardResourceConfiguration is where the various ResourceMethodDispatchAdapters are registerd to enable the following functionality:

- Resource method requests with metrics annotations are delegated to special dispatchets which decorate with metric telemetry
- Resources that return guava optionals are unboxed. Present returns underlying type and non-presents 404s
- Resource methods that are annotated with `@CacheControl` are delegated to a special dispatcher that decorates on the cache control headers
- Enables using Jackson to parse request entities into objects and generate response entities from objects, all while performing validation.


## Dropwizard authentication

Dropwizard support Authenticators.

```
public class ExampleAuthenticator implements Authenticator<BasicCredentials, User> {
    @Override
    public Optional<User> authenticate(BasicCredentials credentials) throws AuthenticationException {
        if ("secret".equals(credentials.getPassword())) {
            return Optional.of(new User(credentials.getUsername()));
        }
        return Optional.empty();
    }
}
```


## Service Discovery

https://github.com/dropwizard/dropwizard-discovery

```
# Discovery-related settings.
discovery:
    serviceName: hello-world
```

```
public class HelloWorldConfiguration extends Configuration {

    @Valid
    @NotNull
    private DiscoveryFactory discovery = new DiscoveryFactory();

    @JsonProperty("discovery")
    public DiscoveryFactory getDiscoveryFactory() {
        return discovery;
    }

    @JsonProperty("discovery")
    public void setDiscoveryFactory(DiscoveryFactory discoveryFactory) {
        this.discovery = discoveryFactory;
    }
}
```

If you only want to register

```
public class HelloWorldApplication extends Application<HelloWorldConfiguration> {

    private final DiscoveryBundle<HelloWorldConfiguration> discoveryBundle = new DiscoveryBundle<HelloWorldConfiguration>() {
        @Override
        public DiscoveryFactory getDiscoveryFactory(HelloWorldConfiguration configuration) {
            return configuration.getDiscoveryFactory();
        }

    };

    @Override
    public void initialize(Bootstrap<HelloWorldConfiguration> bootstrap) {
        bootstrap.addBundle(discoveryBundle);
    }
}
```

If you also want to consume...

```
public class HelloWorldApplication extends Application<HelloWorldConfiguration> {

    private final DiscoveryBundle<HelloWorldConfiguration> discoveryBundle = new DiscoveryBundle<HelloWorldConfiguration>() {
        @Override
        public DiscoveryFactory getDiscoveryFactory(HelloWorldConfiguration configuration) {
            return configuration.getDiscoveryFactory();
        }
    };

    @Override
    public void initialize(Bootstrap<HelloWorldConfiguration> bootstrap) {
        bootstrap.addBundle(discoveryBundle);
    }

    @Override
    public void run(HelloWorldConfiguration configuration, Environment environment) throws Exception {
        final DiscoveryClient client = discoveryBundle.newDiscoveryClient("other-service");
        environment.lifecycle().manage(new DiscoveryClientManager(client));
    }
}
```

```
<dependency>
  <groupId>io.dropwizard.modules</groupId>
  <artifactId>dropwizard-discovery</artifactId>
  <version>1.0.2-1</version>
</dependency>
```

Amazon SDK: mvn -B archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DgroupId=com.folkol.tutorials -DartifactId=awssdk
