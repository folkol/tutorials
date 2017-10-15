package com.folkol.dropwizard;

import io.dropwizard.Application;
import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;

public class tutorialApplication extends Application<tutorialConfiguration> {

    public static void main(final String[] args) throws Exception {
        new tutorialApplication().run(args);
    }

    @Override
    public String getName() {
        return "tutorial";
    }

    @Override
    public void initialize(final Bootstrap<tutorialConfiguration> bootstrap) {
        // TODO: application initialization
    }

    @Override
    public void run(final tutorialConfiguration configuration,
                    final Environment environment) {
        // TODO: implement application
    }

}
