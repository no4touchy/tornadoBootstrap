LESSC := node_modules/less/bin/lessc

BOOTSTRAP_LESS := assets/less/bootstrap.less
BOOTSTRAP_CSS  := assets/css/bootstrap.css

BOOTSTRAP_RESPONSIVE_LESS := assets/less/responsive.less
BOOTSTRAP_RESPONSIVE_CSS  := assets/css/bootstrap-responsive.css

all: css

css:
	@echo -n "Building CSS files from LESS ... "
	@$(LESSC) $(BOOTSTRAP_LESS) > $(BOOTSTRAP_CSS)
	@$(LESSC) $(BOOTSTRAP_RESPONSIVE_LESS) > $(BOOTSTRAP_RESPONSIVE_CSS)
	@echo "Done"

clean:
	@rm -f $(BOOTSTRAP_CSS) $(BOOTSTRAP_RESPONSIVE_CSS)

