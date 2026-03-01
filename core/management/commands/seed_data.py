from django.core.management.base import BaseCommand
from core.models import Service, Project, ProjectImage, TeamMember, Testimonial, CompanyInfo, WhyChooseUs, CoreValue, Post, FAQ
from datetime import date


class Command(BaseCommand):
    help = 'Seed the database with demo data for Kelstech Systems'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        # Services
        services_data = [
            {
                'title': 'CCTV Installation',
                'icon_class': 'fa-video',
                'short_description': 'Professional surveillance camera installation with 24/7 monitoring capabilities and remote viewing options.',
                'full_description': 'Our CCTV installation service provides comprehensive video surveillance solutions for homes, offices, and commercial properties. We use state-of-the-art cameras with HD and 4K resolution, night vision, and remote viewing capabilities.\n\nOur services include:\n• Site assessment and system design\n• IP and analog camera installation\n• DVR/NVR setup and configuration\n• Remote monitoring via mobile app\n• Maintenance and support packages',
                'order': 1,
                'is_featured': True,
            },
            {
                'title': 'Security Systems',
                'icon_class': 'fa-shield-halved',
                'short_description': 'Complete security solutions including access control, alarm systems, and fire detection.',
                'full_description': 'We design and install comprehensive security systems that protect your property and give you peace of mind.\n\nOur offerings include:\n• Access control systems (biometric, card, PIN)\n• Intrusion detection and alarm systems\n• Fire alarm and detection systems\n• Intercom and door entry systems\n• Security audits and consultations',
                'order': 2,
                'is_featured': True,
            },
            {
                'title': 'App Development',
                'icon_class': 'fa-mobile-screen-button',
                'short_description': 'Custom mobile applications for iOS and Android platforms built with the latest technologies.',
                'full_description': 'We build powerful, intuitive mobile applications that help businesses connect with their customers and streamline operations.\n\nOur app development covers:\n• Native iOS and Android development\n• Cross-platform solutions (Flutter, React Native)\n• UI/UX design and prototyping\n• App Store and Play Store publishing\n• Ongoing maintenance and updates',
                'order': 3,
                'is_featured': True,
            },
            {
                'title': 'Website Development',
                'icon_class': 'fa-globe',
                'short_description': 'Modern, responsive websites that drive results — from corporate sites to e-commerce platforms.',
                'full_description': 'We create visually stunning, high-performance websites that represent your brand and convert visitors into customers.\n\nServices include:\n• Corporate and business websites\n• E-commerce platforms\n• Content management systems\n• SEO optimization\n• Website maintenance and hosting',
                'order': 4,
                'is_featured': True,
            },
            {
                'title': 'Software Development',
                'icon_class': 'fa-code',
                'short_description': 'Custom enterprise software solutions, automation tools, and system integrations.',
                'full_description': 'We develop tailored software solutions that automate processes, improve efficiency, and drive business growth.\n\nOur expertise includes:\n• Enterprise resource planning (ERP)\n• Customer relationship management (CRM)\n• Inventory and POS systems\n• Custom database applications\n• API development and integration',
                'order': 5,
                'is_featured': False,
            },
            {
                'title': 'Network Infrastructure',
                'icon_class': 'fa-network-wired',
                'short_description': 'Secure network design, installation, and maintenance for businesses of all sizes.',
                'full_description': 'We build robust, secure network infrastructures that keep your business connected and protected.\n\nServices include:\n• Network design and planning\n• Structured cabling\n• Wi-Fi solutions\n• Server setup and management\n• Network security and firewall configuration',
                'order': 6,
                'is_featured': False,
            },
        ]

        for data in services_data:
            Service.objects.update_or_create(title=data['title'], defaults=data)
        self.stdout.write(self.style.SUCCESS(f'  ✓ {len(services_data)} services created'))

        # Projects
        projects_data = [
            {'title': 'Corporate Office Surveillance', 'description': 'Complete 32-camera CCTV system with remote monitoring for a multinational office complex in Accra.', 'full_description': 'Our team deployed a high-density CCTV network for a flagship corporate office. The project involved 32 IP cameras, advanced motion detection, and a central command center for real-time monitoring. We also integrated mobile access for the security team to view feeds from anywhere.\n\nKey Highlights:\n• High-resolution night vision cameras\n• Integrated backup power system\n• 24/7 technical support\n• Remote access for management', 'client_name': 'Goldfields Ltd', 'category': 'cctv', 'date_completed': date(2025, 8, 15), 'is_featured': True},
            {'title': 'Bank Security Upgrade', 'description': 'Full security overhaul including access control, CCTV, and alarm systems for a major banking institution.', 'full_description': 'A comprehensive security modernization for GCB Bank. We replaced legacy systems with state-of-the-art biometrics, facial recognition cameras, and a secure networked alarm system.\n\nThe project was delivered on schedule with zero downtime during the installation process.', 'client_name': 'GCB Bank', 'category': 'cctv', 'date_completed': date(2025, 6, 10), 'is_featured': True},
            {'title': 'Security Monitoring App', 'description': 'Mobile app for real-time security camera monitoring with push notification alerts and video playback.', 'full_description': 'SafeGuard Solutions requested a bespoke mobile app for their clients to monitor security feeds on the go. We built a native app with ultra-low latency streaming, AES-256 encryption, and an intuitive dashboard.\n\nKey features include:\n• Push notification alerts for motion detection\n• Secure video playback and cloud storage integration\n• Multi-site management from a single interface\n• Cross-platform compatibility (iOS and Android)', 'client_name': 'SafeGuard Solutions', 'category': 'app', 'date_completed': date(2025, 5, 1), 'is_featured': True},
            {'title': 'E-Commerce Platform', 'description': 'Full-featured e-commerce website with inventory management, payment integration, and delivery tracking.', 'full_description': 'A high-performance e-commerce solution for Accra Mall. The platform handles thousands of SKUs and integrates multiple local payment gateways including Mobile Money.\n\nThe project involved building a custom content management system (CMS) tailored to their specific workflow, allowing staff to easily update product listings and track ongoing promotions.', 'client_name': 'Accra Mall', 'category': 'web', 'date_completed': date(2025, 3, 20), 'is_featured': True},
            {'title': 'Inventory Management System', 'description': 'Custom ERP system with real-time stock tracking, automated reordering, and comprehensive reporting.', 'full_description': 'TechMart needed a custom solution to manage their growing inventory across five warehouses. We developed a cloud-based ERP with real-time syncing and automated procurement workflows.\n\nThe system significantly reduced human error and lowered operational costs by automatically generating purchase orders when stock levels dropped below defined thresholds.', 'client_name': 'TechMart Ghana', 'category': 'software', 'date_completed': date(2025, 1, 15), 'is_featured': True},
            {'title': 'Hotel Smart Lock System', 'description': 'Keycard access control system for 120 rooms with central management and audit trail capabilities.', 'full_description': 'Implemented a modern RFID smart lock system for Movenpick Hotel. The system integrates directly with their chosen property management software for seamless check-ins and check-outs.\n\nWe also configured an extensive audit trail feature, giving management complete visibility over room access history to ensure maximum security for guests and staff.', 'client_name': 'Movenpick Hotel', 'category': 'cctv', 'date_completed': date(2014, 11, 5), 'is_featured': True},
        ]

        for data in projects_data:
            project, created = Project.objects.update_or_create(title=data['title'], defaults=data)
            
            # Add dummy gallery images if they don't exist
            if project.images.count() == 0:
                for i in range(1, 4):
                    # We create dummy images even if main image is missing for seed testing
                    ProjectImage.objects.create(
                        project=project,
                        image=project.image if project.image else 'projects/default.jpg',
                        caption=f"Process Shot {i} for {project.title}",
                        order=i
                    )
        self.stdout.write(self.style.SUCCESS(f'  ✓ {len(projects_data)} projects and galleries updated'))

        # Team Members
        team_data = [
            {'name': 'Daniel Kels', 'role': 'Founder & CEO', 'bio': 'Visionary leader with over 10 years of experience in security technology and business management.', 'order': 1},
            {'name': 'Grace Owusu', 'role': 'CTO', 'bio': 'Expert in software architecture and innovative technology solutions with a passion for clean code.', 'order': 2},
            {'name': 'Emmanuel Sekyere', 'role': 'Head of Security Solutions', 'bio': 'Certified security professional specializing in CCTV, access control, and alarm systems.', 'order': 3},
            {'name': 'Abena Frimpong', 'role': 'Lead Developer', 'bio': 'Full-stack developer with expertise in Python, JavaScript, and mobile app development.', 'order': 4},
            {'name': 'Kwesi Mensah', 'role': 'Project Manager', 'bio': 'Experienced project manager who ensures every deployment is on time and within budget.', 'order': 5},
            {'name': 'Ama Serwaa', 'role': 'UI/UX Designer', 'bio': 'Creative designer focused on crafting intuitive, beautiful user experiences.', 'order': 6},
        ]

        for data in team_data:
            TeamMember.objects.update_or_create(name=data['name'], defaults=data)
        self.stdout.write(self.style.SUCCESS(f'  ✓ {len(team_data)} team members created'))

        # Testimonials
        testimonials_data = [
            {'client_name': 'Akosua Mensah', 'company': 'TechHub Ghana', 'quote': 'Kelstech Systems installed a complete surveillance system for our office. Exceptional service, quality equipment, and the team was professional throughout the process.', 'rating': 5},
            {'client_name': 'Kwame Boateng', 'company': 'Safe Logistics', 'quote': 'They built our company\'s mobile app and website from scratch. Professional, fast, and always available for support. Highly recommended!', 'rating': 5},
            {'client_name': 'Efua Asante', 'company': 'GoldStar Ltd', 'quote': 'Their software solution transformed our business operations. The team is incredibly talented, responsive, and truly cares about client satisfaction.', 'rating': 5},
            {'client_name': 'Joseph Kyei', 'company': 'Alpha Schools', 'quote': 'We contracted Kelstech for our school\'s CCTV and access control system. Everything works perfectly and the support team is always a call away.', 'rating': 5},
            {'client_name': 'Nana Esi', 'company': 'Prime Estate', 'quote': 'Outstanding web development work! Our new website has significantly increased our online presence and client inquiries.', 'rating': 4},
            {'client_name': 'Bernard Addo', 'company': 'Metro Hotel', 'quote': 'From security cameras to smart door locks, Kelstech handled everything. A truly one-stop shop for security and tech solutions.', 'rating': 5},
        ]

        for data in testimonials_data:
            Testimonial.objects.update_or_create(client_name=data['client_name'], defaults=data)
        self.stdout.write(self.style.SUCCESS(f'  ✓ {len(testimonials_data)} testimonials created'))

        # Company Info
        CompanyInfo.objects.update_or_create(
            pk=1,
            defaults={
                'company_name': 'Kels Technologies & Systems',
                'about_headline': 'Built on Trust,<br>Driven by Innovation',
                'our_story': '<p>Founded with a vision to bridge the gap between security and technology, Kelstech Systems has grown into a leading provider of comprehensive security installations and cutting-edge software solutions.</p><br><p>Our journey began with CCTV installations, but as technology evolved, so did we. Today, we offer a full spectrum of services — from advanced surveillance systems and access control to custom mobile apps, websites, and enterprise software.</p><br><p>What sets us apart is our commitment to understanding each client\'s unique needs and delivering tailored solutions that exceed expectations.</p>',
                'mission': 'To provide world-class security and technology solutions that protect assets, optimize operations, and drive growth for businesses of all sizes.',
                'vision': 'To be the most trusted name in security technology and software innovation across Africa and beyond.',
                'footer_description': 'Empowering businesses with cutting-edge security solutions and innovative technology services. We build what you need to succeed.',
                'projects_completed': 500,
                'happy_clients': 200,
                'years_experience': 10,
                'team_members_count': 50,
                'address': 'Accra, Ghana',
                'phone': '+233 XX XXX XXXX',
                'email': 'info@kelstechsystems.com',
                'working_hours': 'Mon - Fri: 8:00 AM - 6:00 PM\nSat: 9:00 AM - 2:00 PM',
                'facebook_url': 'https://facebook.com',
                'twitter_url': 'https://twitter.com',
                'instagram_url': 'https://instagram.com',
                'linkedin_url': 'https://linkedin.com',
                'whatsapp_number': '233XXXXXXXXX',
            }
        )
        self.stdout.write(self.style.SUCCESS('  ✓ Company info created'))

        # Why Choose Us
        why_choose_us_data = [
            {'title': 'Certified Professionals', 'icon_class': 'fa-certificate', 'description': 'Our team is certified and trained to handle a wide range of security and tech projects.', 'order': 1},
            {'title': '24/7 Support', 'icon_class': 'fa-headset', 'description': 'Round-the-clock technical support and monitoring for all our clients.', 'order': 2},
            {'title': 'Fast Deployment', 'icon_class': 'fa-bolt', 'description': 'Quick turnaround times without compromising on quality or reliability.', 'order': 3},
        ]
        
        for data in why_choose_us_data:
            WhyChooseUs.objects.update_or_create(title=data['title'], defaults=data)
        self.stdout.write(self.style.SUCCESS(f'  ✓ {len(why_choose_us_data)} Why Choose items created'))

        # Core Values
        core_values_data = [
            {'title': 'Reliability', 'icon_class': 'fa-shield-halved', 'color_class': 'primary', 'description': 'Systems that work when you need them most, backed by robust support.', 'order': 1},
            {'title': 'Innovation', 'icon_class': 'fa-lightbulb', 'color_class': 'accent', 'description': 'Embracing the latest technologies to deliver cutting-edge solutions.', 'order': 2},
            {'title': 'Integrity', 'icon_class': 'fa-handshake', 'color_class': 'green', 'description': 'Transparent dealing and honest communication with every client.', 'order': 3},
            {'title': 'Excellence', 'icon_class': 'fa-trophy', 'color_class': 'yellow', 'description': 'Going beyond expectations in quality, delivery, and service.', 'order': 4},
        ]

        for data in core_values_data:
            CoreValue.objects.update_or_create(title=data['title'], defaults=data)
        self.stdout.write(self.style.SUCCESS(f'  ✓ {len(core_values_data)} Core Values created'))

        # Blog Posts
        posts_data = [
            {'title': 'The Importance of CCTV for Small Businesses', 'author': 'Security Expert', 'category': 'security', 'content': 'Small businesses face unique security challenges. Installing a comprehensive CCTV system is not just about monitoring; it acts as a strong deterrent against theft and vandalism.\n\nHere are 5 reasons why your small business needs CCTV:\n\n1. Deter Crime: Visible cameras prevent incidents.\n2. Remote Monitoring: Keep an eye on your store from your phone.\n3. Evidence Collection: Crucial in case of a break-in.\n4. Protect Employees: Ensures a safe working environment.\n5. Insurance Benefits: Many providers offer discounts for secured premises.\n\nInvest in your business security today.'},
            {'title': 'Top 5 Tech Trends in 2026', 'author': 'Lead Developer', 'category': 'tech', 'content': 'Technology is evolving faster than ever. From AI-driven automation to quantum computing, staying ahead is vital for business success.\n\nIn 2026, we are seeing massive shifts in how mobile applications are built, with hybrid frameworks dominating the market for faster deployment.\n\nSecurity remains a top priority, with Zero Trust architectures becoming the standard across all corporate networks.'},
            {'title': 'Kelstech Systems Expands to New Regions', 'author': 'CEO', 'category': 'company', 'content': 'We are thrilled to announce that Kelstech Systems is officially expanding its branch network to serve more regions.\n\nOur commitment to delivering excellence in security installations and bespoke software development has driven unprecedented growth over the last quarter.\n\nWe look forward to partnering with more businesses and providing world-class tech solutions.'},
        ]
        
        for pdata in posts_data:
            Post.objects.update_or_create(title=pdata['title'], defaults=pdata)
        self.stdout.write(self.style.SUCCESS(f'  ✓ {len(posts_data)} Blog Posts created'))

        # FAQs
        faq_data = [
            {'question': 'What types of areas do you protect with CCTV?', 'answer': 'We install security cameras for a wide range of properties including residential homes, commercial office buildings, industrial warehouses, and retail shops.', 'order': 1},
            {'question': 'Do you provide post-installation support?', 'answer': 'Yes, absolutely. All our installations come with a comprehensive warranty and technical support package to ensure your systems remain operational 24/7.', 'order': 2},
            {'question': 'How long does a website development project take?', 'answer': 'The timeline depends heavily on the project scope. A standard corporate website typically takes 3-4 weeks, whereas complex e-commerce or custom software solutions can take anywhere from 2-6 months.', 'order': 3},
            {'question': 'Do you offer custom mobile app development?', 'answer': 'Yes, our team is proficient in building native and cross-platform mobile apps for both iOS and Android ecosystems to fit your specific business processes.', 'order': 4},
            {'question': 'Can I request a free consultation before committing?', 'answer': 'Yes! We believe in transparent communication. You can reach out to us via our contact form or give us a call to schedule a free initial consultation to discuss your needs.', 'order': 5},
        ]
        for fdata in faq_data:
            FAQ.objects.update_or_create(question=fdata['question'], defaults=fdata)
        self.stdout.write(self.style.SUCCESS(f'  ✓ {len(faq_data)} FAQs created'))

        self.stdout.write(self.style.SUCCESS('\n✅ Database seeded successfully!'))
