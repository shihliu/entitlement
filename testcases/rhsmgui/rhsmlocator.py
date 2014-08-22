class RHSMLocator:
	# ========================================================
	#       RHSM GUI test elements
	# ========================================================
	get_window = {
	######## For RHEL 5.X RHSM object locator ########
	'main-window-5.10':		      'Subscription Manager',
	'register-dialog-5':		     'register_dialog',
	'subscribe-dialog-5':		    'Subscribe System',
	
	######## For RHEL 6.X RHSM object locator ########
	'main-window-6':			 'frmSubscriptionManager',
	'register-dialog-6':		     'dlgregister_dialog',
	'subscribe-dialog-6':		    'frmSubscribeSystem',
	'import-certificate-dialog-6':	   'dlgProvideaSubscriptionCertificate',
	'import-cert-dialog-6':		  'dlgImportCertificates',
	'select-file-dialog-6':		  'dlgSelectAFile',
	'system-facts-dialog-6':		 'dlgfacts_dialog',
	'search-dialog-6':		       'frmSearching',
	'proxy-configuration-dialog-6':	  'dlgProxyConfiguration',
	'information-dialog-6':		  'dlgInformation',
	'question-dialog-6':		     'dlgQuestion',
	'error-dialog-6':			'dlgError',
	'system-preferences-dialog-6':	   'dlgSystemPreferences',
	'subscription-manager-manual-window-6':  'frmSubscriptionManagerManual',
	'onlinedocumentation-window-6':	  'frmRedHatSubscriptionManagement-RedHatCustomerPortal-MozillaFireFox',
	'security-warning-dialog-6':	     'dlgSecurityWarning',
	'about-subscription-manager-dialog-6':   'dlgAboutSubscriptionManager',
	'rhsm-notification-dialog-6':	    'dlgNotification',
	'filter-options-window-6':	       'frmFilterOptions',
	'error-cert-dialog-6':		   'dlgError',
	'sm-gui-warning-classic-dialog-6':	      'dlgWarning',
	#### window in firstboot gui for RHEL6.4
	'firstboot-main-window-6':			       'frm0',
	'firstboot-wng-dialog-6':				'dlgWarning',
	'firstboot-err-dialog-6':				'dlgError',
	# ## window in rhn-classic gui for RHEL6.4
	"classic-main-window-6":		"frmSystemRegistration",
	"classic-confirm-osrelease-window-6":		"dlgConfirmoperationsystemreleaseselection",
	"classic-updates-configured-window-6":		"frmUpdatesConfigured",
	}

	get_tab = {
	######## For RHEL 5.X RHSM object locator ########
	'all-tabs-5':			    'ptl0',
	'my-installed-software-5':	       'My Installed Products',
	'my-subscriptions-5':		    'My Subscriptions',
	'all-available-subscriptions-5':	 'All Available Subscriptions',
	######## For RHEL 6.X RHSM object locator ########
	'all-tabs-6':			    'ptl0',
	'my-installed-software-6':	       'ptabMyInstalledSoftware',
	'my-installed-software-6.4':	     'ptabMyInstalledProducts',
	'my-subscriptions-6':		    'ptabMySubscriptions',
	'all-available-subscriptions-6':	 'ptabAllAvailableSubscriptions',
	}

	get_button = {
	######## For RHEL 5.X RHSM object locator ########
	# button in main window
	'register-button-5':		     'Register System',
	'unregister-button-5':		   'btnUnregister',
	'auto-subscribe-button-5':	       'Auto-subscribe',
	'unsubscribe-button-5':		  'btnUnsubscribe',
	# button in register dialog
	'dialog-register-button-5':	      'register_button',
	'dialog-cancle-button-5':		'cancel_button',
	# button in subscribe dialog
	'dialog-subscribe-button-5':	     'btnSubscribe',
	'dialog-back-button-5':		  'btnBack',
	'dialog-cancle-button-5':		'btnCancel',
	######## For RHEL 6.X RHSM object locator ########
	# button in main window
	'register-button-6':		     'btnRegister',
	'register-button-6.4':		   'btnRegisterSystem',
	'unregister-button-6':		   'btnUnregister',
	'auto-subscribe-button-6':	       'btnAuto-subscribe',
	'auto-subscribe-button-6.4':	     'btnAuto-attach',
	# 'unsubscribe-button-6':		  'btnUnsubscribe',
	'remove-subscriptions-button-6':	 'btnRemove',
	'system-preferences-button-6':	   'btnSystemPreferences',
	'proxy-configuration-button-6':	  'btnProxyConfiguration',
	'view-system-facts-button-6':	    'btnViewSystemFacts',
	'import-certificate-button-6':	   'btnImportCertificate',
	'help-button-6':			 'btnHelp',
	'update-button-6':		       'btnSearch',
	'filters-button-6':		      'btnFilters',
	# button in register dialog
	'dialog-register-button-6':	      'btnregisterbutton',
	'configure-proxy-button-6':	      'btnproxybutton',
	'dialog-cancle-button-6':		'btncancelbutton',
	# button in subscribe dialog
	'dialog-subscribe-button-6':	     'btnSubscribe',
	'dialog-back-button-6':		  'btnBack',
	'dialog-cancle-button-6':		'btnCancel',
	'dialog-cancle-button-6.4':	      'btncancelbutton',
	# button in import-certificate-dialog
	'ok-button-6':			   'btnOK',
	'import-file-button-6':		  'btnImport',
    'type-pem-name-button-6':		'tbtnTypefilename',
	'certificate-location-button-6':	 'btn(None)',
	# button in select-file-dialog
	'type-file-name-button-6':	       'tbtnTypeafilename',
	'open-file-button-6':		    'btnOpen',
	'open-file-button-6.4':		  'btnImport',
	'proxy-close-button-6':		  'btnCloseButton',
	'yes-button-6':			  'btnYes',
	# button in system-preferences-dialog
	'close-button-6':			'btnClose',
	#### button in firstboot gui for RHEL6.4
	'firstboot-fwd-button-6':				'btnForward',
	'firstboot-agr-button-6':				'rbtnYes,IagreetotheLicenseAgreement',
	'firstboot-yes-button-6':				'btnYes',
	'firstboot-ok-button-6':				 'btnOK',
	'firstboot-finish-button-6':		     'btnFinish',
	'firstboot-register-now-button-6':			 "rbtnYes,I'dliketoregisternow",
	'firstboot-register-rhsm-button-6':			 'rbtnRedHatSubscriptionManagement',
	"firstboot-classic-select-button-6":		"rbtnRedHatNetwork(RHN)Classic",
	#### button in rhn_classic gui for RHEL6.4
	"classic-forward-button-6":		"btnForward",
	"classic-confirm-osrelease-yes-button-6":		"btnYes,Continue",
	"classic-updates-configured-finish-button-6":		"btnFinish",
	}

	get_table = {
	######## For RHEL 5.X RHSM object locator ########
	'my-product-table-5':		    'Installed View',
	'my-subscription-table-5':	       'My Subscriptions View',
	'all-subscription-table-5':	      'AllSubscriptionsView',
	'all-product-table-5':		   'tblAllAvailableBundledProductTable',
	'installed-product-table-5':	     'tblInstalledView',
	######## For RHEL 6.X RHSM object locator ########
	'my-product-table-6':		    'tblBundledProductsTable',
	'my-subscription-table-6':	       'ttblMySubscriptionsView',
	'all-subscription-table-6':	      'ttblAllSubscriptionsView',
	'all-product-table-6':		   'tblAllAvailableBundledProductTable',
	'installed-product-table-6':	     'tblInstalledView',
	'facts-view-table-6':		    'ttblfactsview',
	'orgs-view-table-6':		     'tblownertreeview',
	}

	get_text = {
	######## For RHEL 5.X RHSM object locator ########
	'login-text-5':			  'txtaccountlogin',
	'password-text-5':		       'txtaccountpassword',
	######## For RHEL 6.X RHSM object locator ########
	'login-text-6':			  'account_login',
	'password-text-6':		       'account_password',
	# text in select-file-dialog
	'location-text-6':		       'txtLocation',
	'proxy-location-text-6':		 'txtProxyLocation',
	'server-url-text-6':		     'txtserverentry',
	# firstboot for RHEL6.4
	'firstboot-login-text-6':		 'txtaccountlogin',
	'firstboot-password-text-6':		 'txtaccountpassword',
	# rhn_classic for RHEL6.4 ; firstboot-classic for RHEL6.4
	"classic-login-text-6":		"txtLogin",
	"classic-password-text-6":		"txtPassword",
	"classic-set-systemname-text-6":		"txtSystemName",
	
	}

	get_menu = {
	######## For RHEL 5.X RHSM object locator ########
	######## For RHEL 6.X RHSM object locator ########
	# under System menu
	'system-menu-6':			   'mnuSystem',
	'register-menu-6':			 'mnuRegister',
	'unregister-menu-6':		       'mnuUnregister',
	'importcert-menu-6':		       'mnuImportCert',
	'viewsystemfacts-menu-6':		  'mnuViewSystemFacts',
	'configureproxy-menu-6':		   'mnuConfigureProxy',
	'preferences-menu-6':		      'mnuPreferences',
	'quit-menu-6':			     'mnuQuit',
	# under Help menu
	'help-menu-6':			     'mnuHelp',
	'gettingstarted-menu-6':		   'mnuGettingStarted',
	'onlinedocumentation-menu-6':	      'mnuOnlineDocumentation',
	'about-menu-6':			    'mnuAbout',
	# service level menu
	'notset-menu-6':			   'mnuNotSet',
	'premium-menu-6':			  'mnuPremium',
	# release version menu
	'61-menu-6':			       'mnu61',
	'62-menu-6':			       'mnu62',
	'63-menu-6':			       'mnu63',
	'64-menu-6':			       'mnu64',
	'6server-menu-6':			  'mnu6Server',
	# import cert
	'ImportCertificate-menu-6':		'mnuImportCert',
	}

	get_checkbox = {
	######## For RHEL 5.X RHSM object locator ########
	######## For RHEL 6.X RHSM object locator ########
	'manual-attach-checkbox-6':		'chkautobind',
	'proxy-checkbox-6':			'chkProxyCheckbox',
	'match-system-checkbox-6':		 'chkMatchSystem',
	'match-installed-checkbox-6':	      'chkMatchInstalled',
	'do-not-overlap-checkbox-6':	       'chkDoNotOverlap',
	# ##firstboot checkbox for RHEL6.4
	'firstboot-manual-checkbox-6':		   'chkautobind',
	'firstboot_activationkey-checkbox-6':	   'chkIwilluseanActivationKey',

	}

	get_label = {
	######## For RHEL 5.X RHSM object locator ########
	######## For RHEL 6.X RHSM object locator ########
	'import-cert-success-label-6':	      	'lblCertificateimportwassuccessful',
	'register-error-label-6':		   	'lblUnabletoregisterthesystemInvalidusernameorpasswordTocreatealogin,pleasevisithttps//wwwredhatcom/wapps/ugc/registerhtmlPleasesee/var/log/rhsm/rhsmlogformoreinformation',
	'search-subscriptions-hint-label-6':		'lbl2applied',
	'error-user-label-6':			   'lblUserusertestisnotabletoregisterwithanyorgs',
	'warning-classic-already-label-6':	      'lblWARNINGThissystemhasalreadybeenregisteredwithRedHatusingRHNClassicThetoolyouareusingisattemptingtore-registerusingRedHatSubscriptionManagementtechnologyRedHatrecommendsthatcustomersonlyregisteronceTolearnhowtounregisterfromeitherservicepleaseconsultthisKnowledgeBaseArticlehttps//accessredhatcom/kb/docs/DOC-45563',
	###### firstboot label in RHEL6.4
	'firstboot-registeration-warning-label-6':  	'lblYoursystemwasregisteredforupdatesduringinstallation',
	'firstboot_creat_user-label-6':	     	"lblYoumustcreatea'username'forregular(non-administrative)useofyoursystemTocreateasystem'username',pleaseprovidetheinformationrequestedbelow",
	'firstboot-skip-auto-label-6':		    		"lblYouhaveoptedtoskipauto-attach",
	"firstboot-classic-reviewsubscription-label-6":		"lblReviewSubscription",
	"firstboot-classic-finishupdate-label-6":			"lblFinishUpdatesSetup",
	###### rhn_classic label in RHEL6.4
	"classic-software-update-label-6":		"lblSetUpSoftwareUpdates",
	"classic-choose-service-label-6":		"lblChooseService",
	"classic-redhat-account-label-6":		"lblRedHatAccount",
	"classic-OS-realeaseversion-label-6":		"lblOperatingSystemReleaseVersion",
	"classic-create-profile-label-6":		"lblCreateProfile",
	"classic-review-subscription-label-6":		"lblReviewSubscription",
	}

	get_combobox = {
	######## For RHEL 5.X RHSM object locator ########
	######## For RHEL 6.X RHSM object locator ########
	'service-level-notset-combobox-6':	  'cboNotSet',
	'service-level-premium-combobox-6':	 'cboPremium',
	'service-level-none-combobox-6':	    'cboNone',
	'release-version-combobox-6':	       'cbo1',
	'release-version-6server-combobox-6':       'cbo6Server',
	}
	get_progressbar = {
	##for RHEL 6.x ####
	'register-progressbar-6':		   'pbarregisterprogressbar',

	}
