udevrulesdir = $(sysconfdir)/udev/rules.d
dist_udevrules_DATA = 55-DLiD4000.rules

EXTRA_DIST = multiload.conf.add

multiloaddir = $(sysconfdir)
multiload_DATA = multiload.conf

multiload.conf: $(srcdir)/multiload.conf.add
	if test -a @sysconfdir@/multiload.conf; then \
		if ! grep -q "Discovery D4000" @sysconfdir@/multiload.conf; then \
			cat @sysconfdir@/multiload.conf $(srcdir)/multiload.conf.add > multiload.conf ; \
		else \
			cp @sysconfdir@/multiload.conf . ; \
		fi ; \
	else \
		cp $(srcdir)/multiload.conf.add multiload.conf ; \
	fi


clean-local:
	rm -f multiload.conf

distclean-local:
	rm -f multiload.conf

