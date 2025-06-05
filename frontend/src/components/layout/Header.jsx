import { Box, Flex, Heading, Spacer, Button } from '@chakra-ui/react';
import { Link as RouterLink } from 'react-router-dom';

/**
 * Header component for the application
 * 
 * @returns {JSX.Element} Header component
 */
const Header = () => {
  return (
    <Box as="header" bg="brand.600" color="white" p={4} boxShadow="md">
      <Flex maxW="1200px" mx="auto" align="center">
        <Heading as="h1" size="lg">
          <RouterLink to="/">TURBO_AML</RouterLink>
        </Heading>
        <Spacer />
        <Button
          as={RouterLink}
          to="/"
          variant="ghost"
          color="white"
          _hover={{ bg: 'brand.700' }}
        >
          Home
        </Button>
      </Flex>
    </Box>
  );
};

export default Header; 